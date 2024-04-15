import asyncio
import itertools
from urllib.parse import urlparse
from typing import Callable, Awaitable, Optional, Dict

from fxsdk.client.http import RpcRequest, HttpRpcClient
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
    __doc__ = HttpRpcClient.__doc__

    @classmethod
    async def create(cls, endpoint_url: str, loop, callback: Callable[[Dict], Awaitable[None]] = None):
        self = WebsocketRpcClient()
        loop = loop if loop else asyncio.get_event_loop()
        callback = callback if callback else self.receive
        self._conn = ReconnectingRpcWebsocket(endpoint_url, loop=loop, recv=callback)
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
        await self._conn.send_rpc_message('status')

    async def get_health(self):
        await self._conn.send_rpc_message('health')

    async def get_unconfirmed_txs(self):
        await self._conn.send_rpc_message('unconfirmed_txs')

    async def get_validators(self, height: int, page: int = 1):
        data = {
            'height': str(height),
            'page': str(page),
            'per_page': '30'
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

    async def get_block_header(self, height: Optional[int] = None):
        data = {
            'height': str(height) if height else None
        }
        await self._conn.send_rpc_message('block_header', data)

    async def get_block(self, height: Optional[int] = None):
        data = {
            'height': str(height) if height else None
        }
        await self._conn.send_rpc_message('block', data)

    async def block_search(self, query: str, prove: Optional[bool] = None,
                           page: Optional[int] = None, per_page: Optional[int] = None,
                           order_by: Optional[str] = None):
        data = {
            'query': query
        }
        if prove:
            data['prove'] = str(prove)
        if page:
            data['page'] = str(page)
        if per_page:
            data['per_page'] = str(per_page)
        if order_by:
            data['order_by'] = order_by

        await self._conn.send_rpc_message('block_search', data)

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

    async def check_tx(self, tx: Tx):
        tx_raw = TxRaw(
            body_bytes=tx.body.SerializeToString(),
            auth_info_bytes=tx.auth_info.SerializeToString(),
            signatures=tx.signatures,
        )
        tx_bytes = tx_raw.SerializeToString()
        data = {
            'tx': '0x' + tx_bytes.hex(),
        }
        await self._conn.send_rpc_message('check_tx', data)

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
                        page: Optional[int] = None, per_page: Optional[int] = None,
                        order_by: Optional[str] = None):
        data = {
            'query': query
        }
        if prove:
            data['prove'] = str(prove)
        if page:
            data['page'] = str(page)
        if per_page:
            data['per_page'] = str(per_page)
        if order_by:
            data['order_by'] = order_by

        await self._conn.send_rpc_message('tx_search', data)
