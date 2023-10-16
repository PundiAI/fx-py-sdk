import asyncio
import logging.config
from typing import Dict

import yaml

from fxsdk.client.websockets import WebsocketRpcClient, ReconnectingRpcWebsocket
from fxsdk.msg import event, new_tx_from_base64
from fxsdk.x.cosmos.bank.v1beta1.tx_pb2 import MsgSend


class BlockchainEvent(WebsocketRpcClient):

    @classmethod
    async def create(cls, endpoint_url: str, loop, callback=None):
        self = BlockchainEvent()
        loop = loop if loop else asyncio.get_event_loop()
        callback = callback if callback else self.receive
        self._conn = ReconnectingRpcWebsocket(endpoint_url, loop=loop, recv=callback)
        return self

    async def receive(self, data: Dict):
        self._log.info(f"received data: {data}")
        result = data.get('result', {})
        query = result.get('query', '')
        value = result.get('data', {}).get('value', {})
        if query == event.EVENT_NEW_BLOCK_HEADER:
            self.process_new_block_header(value)
        elif query == event.EVENT_NEW_BLOCK_EVENTS:
            self.process_new_block_events(value)
        elif query == event.EVENT_NEW_BLOCK:
            self.process_new_block(value)
        elif query == event.EVENT_TX:
            self.process_tx(value)

    async def subscribe_new_block_header(self):
        await self.subscribe(event.EVENT_NEW_BLOCK_HEADER)

    def process_new_block_header(self, data: Dict):
        height = data.get('header', {}).get('height', 0)
        block_time = data.get('header', {}).get('time', '')
        self._log.info(f"new block header: height={height}, block_time={block_time}")

    async def subscribe_new_block_events(self):
        await self.subscribe(event.EVENT_NEW_BLOCK_EVENTS)

    def process_new_block_events(self, data: Dict):
        height = data.get('height', 0)
        events = data.get('events', [])
        num_txs = data.get('num_txs', 0)
        self._log.info(f"new block events: height={height}, events={len(events)}, num_txs={num_txs}")

    async def subscribe_new_block(self):
        await self.subscribe(event.EVENT_NEW_BLOCK)

    def process_new_block(self, data: Dict):
        block = data.get('block', {})
        height = block.get('header', {}).get('height', 0)
        block_time = block.get('header', {}).get('time', '')
        base64_txs = block.get('data', {}).get('txs', [])
        txs = []
        for base64_tx in base64_txs:
            tx = new_tx_from_base64(base64_tx)
            txs.append(tx)
        events = data.get('result_finalize_block', {}).get('events', [])
        self._log.info(f"new block: height={height}, block_time={block_time}, txs={len(txs)}, events={len(events)}")

    async def subscribe_tx(self):
        await self.subscribe(event.EVENT_TX)

    def process_tx(self, data: Dict):
        height = data.get('TxResult', {}).get('height', 0)
        events = data.get('TxResult', {}).get('result', {}).get('events')
        base64_tx = data.get('TxResult', {}).get('tx', '')
        tx = new_tx_from_base64(base64_tx)
        for msg in tx.body.messages:
            if msg.type_url == '/cosmos.bank.v1beta1.MsgSend':
                msg_send = MsgSend()
                msg_send.ParseFromString(msg.value)
                self._log.info(f"new tx: height={height}, tx={msg_send}, events={events}")
                break


global_loop = None


async def main():
    global global_loop
    rpc_url = "http://127.0.0.1:26657"
    ws_client = await BlockchainEvent.create(endpoint_url=rpc_url, loop=global_loop)
    await ws_client.subscribe_new_block()

    while True:
        logging.info("sleeping to keep loop open")
        await asyncio.sleep(5)


if __name__ == '__main__':
    logging.config.dictConfig(yaml.safe_load(open('../.logging.yaml', 'r')))
    global_loop = asyncio.get_event_loop()
    global_loop.run_until_complete(main())
