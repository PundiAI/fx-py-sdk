import asyncio
import itertools
from urllib.parse import urlparse
from typing import Callable, Awaitable, Optional, Dict

from fxsdk.client.http import RpcRequest
from fxsdk.msg import event
from fxsdk.websockets import ReconnectingWebsocket, WebsocketManagerBase
from fxsdk.x.cosmos.tx.v1beta1.service_pb2 import BroadcastMode, BROADCAST_MODE_SYNC, BROADCAST_MODE_ASYNC, \
    BROADCAST_MODE_BLOCK
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import Tx, TxRaw


class WebsocketException(Exception):
    pass


class ReconnectingRpcWebsocket(ReconnectingWebsocket):
    id_generator = itertools.count(1)

    def _get_ws_endpoint_url(self):
        o = urlparse(self._endpoint_url)
        if o.scheme == 'http' or o.scheme == 'tcp':
            return f"ws://{o.netloc}/websocket"
        elif o.scheme == 'https':
            return f"wss://{o.netloc}/websocket"
        return f"{self._endpoint_url}/websocket"

    async def send_keepalive(self):
        await self.send_rpc_message('keepAlive')

    async def send_rpc_message(self, method, params=None, retry_count=0):
        if not self._socket:
            if retry_count < self._retry_count:
                await asyncio.sleep(1)
                await self.send_rpc_message(method, params, retry_count + 1)
            else:
                raise WebsocketException("Unable to send, not connected")
        else:
            req = RpcRequest(method, next(self.id_generator), params)
            await self._socket.send(str(req))

    async def ping(self):
        await self.send_rpc_message('ping')


class WebsocketRpcClient(WebsocketManagerBase):

    @classmethod
    async def create(cls, endpoint_url: str, callback: Callable[[Dict], Awaitable[None]] = None, loop=None):
        """Create a WebsocketRpcClient instance

        :param endpoint_url: node endpoint url
        :param loop: asyncio loop
        :param callback: async callback function to receive messages
        :return:
        """
        self = WebsocketRpcClient(endpoint_url)
        loop = loop if loop else asyncio.get_event_loop()
        callback = callback if callback else self.receive
        self._conn = ReconnectingRpcWebsocket(endpoint_url, recv=callback, loop=loop)
        return self

    async def close(self):
        try:
            await self.unsubscribe_all()
            await self._conn.cancel()
        except WebsocketException:
            pass

    async def subscribe(self, query):
        req_msg = {
            "query": query
        }
        await self._conn.send_rpc_message('subscribe', req_msg)

    async def unsubscribe(self, query):
        req_msg = {
            "query": query
        }
        await self._conn.send_rpc_message('unsubscribe', req_msg)

    async def unsubscribe_all(self):
        await self._conn.send_rpc_message('unsubscribe_all')

    async def get_abci_info(self):
        await self._conn.send_rpc_message('abci_info')

    async def get_consensus_state(self):
        await self._conn.send_rpc_message('consensus_state')

    async def dump_consensus_state(self):
        await self._conn.send_rpc_message('dump_consensus_state')

    async def get_genesis(self):
        await self._conn.send_rpc_message('genesis')

    async def get_net_info(self):
        await self._conn.send_rpc_message('net_info')

    async def get_num_unconfirmed_txs(self):
        await self._conn.send_rpc_message('num_unconfirmed_txs')

    async def get_status(self):
        await self._conn.send_rpc_message(method='status')

    async def get_health(self):
        await self._conn.send_rpc_message('health')

    async def get_unconfirmed_txs(self):
        await self._conn.send_rpc_message('unconfirmed_txs')

    async def get_validators(self, height: int, page: int = 1):
        data = {
            'height': str(height),
            'page': str(page),
            'per_page': '10'
        }
        await self._conn.send_rpc_message('validators', data)

    async def abci_query(self, data: str, path: Optional[str] = None,
                         prove: Optional[bool] = None, height: Optional[int] = None):
        data = {
            'data': data
        }
        if path:
            data['path'] = path
        if prove:
            data['prove'] = str(prove)
        if height:
            data['height'] = str(height)

        await self._conn.send_rpc_message('abci_query', data)

    async def get_block(self, height: Optional[int] = None):
        data = {
            'height': str(height) if height else None
        }
        await self._conn.send_rpc_message('block', data)

    async def get_block_results(self, height: int):
        data = {
            'height': str(height)
        }
        await self._conn.send_rpc_message('block_results', data)

    async def get_block_commit(self, height: int):
        data = {
            'height': str(height)
        }
        await self._conn.send_rpc_message('commit', data)

    async def get_blockchain_info(self, min_height: int, max_height: int):
        assert max_height > min_height

        data = {
            'minHeight': str(min_height),
            'maxHeight': str(max_height)
        }
        await self._conn.send_rpc_message('blockchain', data)

    async def broadcast_tx(self, tx: Tx, mode: BroadcastMode = BROADCAST_MODE_SYNC):
        tx_raw = TxRaw(
            body_bytes=tx.body.SerializeToString(),
            auth_info_bytes=tx.auth_info.SerializeToString(),
            signatures=tx.signatures,
        )
        tx_bytes = tx_raw.SerializeToString()
        data = {
            'tx': '0x' + tx_bytes.hex(),
        }
        if mode == BROADCAST_MODE_SYNC:
            return await self._broadcast_tx_sync(data)
        elif mode == BROADCAST_MODE_ASYNC:
            return await self._broadcast_tx_async(data)
        elif mode == BROADCAST_MODE_BLOCK:
            return await self._broadcast_tx_commit(data)

    async def _broadcast_tx_async(self, tx_data: Dict):
        await self._conn.send_rpc_message('broadcast_tx_async', tx_data)

    async def _broadcast_tx_commit(self, tx_data: Dict):
        await self._conn.send_rpc_message('broadcast_tx_commit', tx_data)

    async def _broadcast_tx_sync(self, tx_data: Dict):
        await self._conn.send_rpc_message('broadcast_tx_sync', tx_data)

    async def get_consensus_params(self, height: Optional[int] = None):
        data = {
            'height': str(height) if height else None
        }
        await self._conn.send_rpc_message('consensus_params', data)

    async def get_tx(self, tx_hash: str, prove: Optional[bool] = None):
        data = {
            'hash': tx_hash
        }
        if prove:
            data['prove'] = str(prove)

        await self._conn.send_rpc_message('tx', data)

    async def tx_search(self, query: str, prove: Optional[bool] = None,
                        page: Optional[int] = None, limit: Optional[int] = None):
        data = {
            'query': query
        }
        if prove:
            data['prove'] = str(prove)
        if page:
            data['page'] = str(page)
        if limit:
            data['limit'] = str(limit)

        await self._conn.send_rpc_message('tx_search', data)


class BlockchainEvent(WebsocketRpcClient):

    @classmethod
    async def create(cls, endpoint_url: str, callback=None, loop=None):
        """Create a WebsocketManagerBase instance

        :param endpoint_url: node endpoint url
        :param loop: asyncio loop
        :param callback: async callback function to receive messages
        :return:
        """
        self = WebsocketManagerBase(endpoint_url)
        loop = loop if loop else asyncio.get_event_loop()
        callback = callback if callback else self.receive
        self._conn = ReconnectingWebsocket(endpoint_url, recv=callback, loop=loop)
        return self

    def receive(self, data: Dict):
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
        txs = block.get('data', {}).get('txs', [])
        events = data.get('result_finalize_block', {}).get('events', [])
        self._log.info(f"new block: height={height}, block_time={block_time}, txs={len(txs)}, events={len(events)}")

    async def subscribe_tx(self):
        await self.subscribe(event.EVENT_TX)

    def process_tx(self, data: Dict):
        height = data.get('TxResult', {}).get('height', 0)
        base64_tx = data.get('TxResult', {}).get('tx', '')
        events = data.get('TxResult', {}).get('result', {}).get('events')
        self._log.info(f"new tx: height={height}, tx={base64_tx}, events={events}")
