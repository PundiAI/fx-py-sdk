import asyncio
import itertools
import json
import traceback
from typing import Optional, Dict

import aiohttp
import requests
import ujson
from requests.sessions import ChunkedEncodingError, HTTPAdapter
from urllib3.util.retry import Retry

from jsonrpc.request import RpcRequest

requests.models.json = ujson


def _get_headers():
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }


class BaseHttpRpcClient:
    id_generator = itertools.count(1)

    def __init__(self, endpoint_url, requests_params: Optional[Dict] = None):
        self._endpoint_url = endpoint_url
        self._requests_params = requests_params

        self.session = self._init_session()

    def _init_session(self):

        session = requests.session()
        session.headers.update(_get_headers())
        return session

    def _get_rpc_request(self, path, **kwargs) -> str:

        rpc_request = RpcRequest(path, next(self.id_generator), kwargs.get('data', None))

        return str(rpc_request)

    def request_kwargs(self, method, **kwargs):

        # set default requests timeout
        kwargs['timeout'] = 10

        # add our global requests params
        if self._requests_params:
            kwargs.update(self._requests_params)

        kwargs['data'] = kwargs.get('data', {})
        kwargs['headers'] = kwargs.get('headers', {})

        if kwargs['data'] and method == 'get':
            kwargs['params'] = kwargs['data']
            del (kwargs['data'])

        if method == 'post':
            kwargs['headers']['content-type'] = 'text/plain'

        return kwargs


class HttpRpcClient(BaseHttpRpcClient):

    def __init__(self, endpoint_url, requests_params: Optional[Dict] = None, max_retries=3):
        super(HttpRpcClient, self).__init__(endpoint_url, requests_params)
        if max_retries:
            retries = Retry(total=max_retries,
                            backoff_factor=.5,
                            status_forcelist=[500, 502, 503, 504])
            self.session.mount('http://', HTTPAdapter(max_retries=retries))

    def _request(self, path, **kwargs):

        rpc_request = self._get_rpc_request(path, **kwargs)
        try:
            response = self.session.post(self._endpoint_url, data=rpc_request.encode(), headers=_get_headers())
        except ChunkedEncodingError as ex:
            print(f'Error getting {json.loads(rpc_request)["params"]["height"]}')
            traceback.print_exc()

        return self._handle_response(response)

    def _request_session(self, path, params=None):

        kwargs = {
            'params': params,
            'headers': _get_headers()
        }

        response = self.session.get(f"{self._endpoint_url}/{path}", **kwargs)

        return self._handle_session_response(response)

    @staticmethod
    def _handle_response(response):
        """Internal helper for handling API responses from the server.
        Raises the appropriate exceptions when necessary; otherwise, returns the
        response.
        """

        try:
            res = response.json()

            if 'error' in res and res['error']:
                raise Exception(response)

            # by default return full response
            # if it's a normal response we have a data attribute, return that
            if 'result' in res:
                res = res['result']
            return res
        except ValueError:
            raise Exception('Invalid Response: %s' % response.text)

    @staticmethod
    def _handle_session_response(response):
        """Internal helper for handling API responses from the server.
        Raises the appropriate exceptions when necessary; otherwise, returns the
        response.
        """

        if not str(response.status_code).startswith('2'):
            raise Exception(response)
        try:
            res = response.json()

            if 'code' in res and res['code'] != "200000":
                raise Exception(response)

            if 'success' in res and not res['success']:
                raise Exception(response)

            # by default return full response
            # if it's a normal response we have a data attribute, return that
            if 'result' in res:
                res = res['result']
            return res
        except ValueError:
            raise Exception('Invalid Response: %s' % response.text)

    def get_path_list(self):
        """Return HTML formatted list of available endpoints
        """
        res = self._request(self._endpoint_url, method="get")
        return res.content

    def get_abci_info(self):
        """Get some info about the application.
        """
        return self._request('abci_info')

    def get_consensus_state(self):
        """ConsensusState returns a concise summary of the consensus state. UNSTABLE
        """
        return self._request('consensus_state')

    def dump_consensus_state(self):
        """DumpConsensusState dumps consensus state. UNSTABLE
        """
        return self._request('dump_consensus_state')

    def get_genesis(self):
        """Get genesis file.
        """
        return self._request('genesis')

    def get_net_info(self):
        """Get network info.
        """
        return self._request('net_info')

    def get_num_unconfirmed_txs(self):
        """Get number of unconfirmed transactions.
        """
        return self._request('num_unconfirmed_txs')

    def get_status(self):
        """Get Tendermint status including node info, pubkey, latest block hash, app hash, block height and time.
        """
        return self._request('status')

    def get_health(self):
        """Get node health. Returns empty result (200 OK) on success, no response - in case of an error.
        """
        return self._request('health')

    def get_unconfirmed_txs(self):
        """Get unconfirmed transactions (maximum ?limit entries) including their number.
        """
        data = {
            'limit': str('100'),
        }
        return self._request('unconfirmed_txs', data=data)

    def get_validators(self, height: int, page: int = 1):
        """Get the validator set at the given block height. If no height is provided, it will fetch the
        current validator set.
        """
        data = {
            'height': str(height),
            'page': str(page),
            'per_page': '10'
        }
        return self._request('validators', data=data)

    def abci_query(self, data: str, path: Optional[str] = None,
                   prove: Optional[bool] = None, height: Optional[int] = None):
        """Query the application for some information.

        path	string	Path to the data ("/a/b/c")
        data	[]byte	Data
        height	int64	Height (0 means latest)
        prove	bool	Includes proof if true
        """

        data = {
            'data': data
        }
        if path:
            data['path'] = path
        if prove:
            data['prove'] = str(prove)
        if height:
            data['height'] = str(height)

        return self._request('abci_query', data=data)

    def get_block(self, height: Optional[int] = None):
        """Get block at a given height. If no height is provided, it will fetch the latest block.

        height	int64
        """

        data = {
            'height': str(height) if height else None
        }

        return self._request('block', data=data)

    def get_block_results(self, height: int):
        """BlockResults gets ABCIResults at a given height.
        If no height is provided, it will fetch results for the latest block.

        height	int64
        """

        data = {
            'height': str(height)
        }

        return self._request('block_results', data=data)

    def get_block_commit(self, height: int):
        """Get block commit at a given height. If no height is provided, it will fetch the commit for the latest block.

        height	int64	0

        """

        data = {
            'height': str(height)
        }

        return self._request('commit', data=data)

    def get_blockchain_info(self, min_height: int, max_height: int):
        """Get block headers for minHeight <= height <= maxHeight. Block headers are returned in descending order
        (highest first). Returns at most 20 items.

        min_height	int64	0
        max_height	int64	0

        """

        assert max_height > min_height

        data = {
            'minHeight': str(min_height),
            'maxHeight': str(max_height)
        }

        return self._request('blockchain', data=data)

    def _broadcast_tx_async(self, tx_data: Dict):
        """Returns right away, with no response
        """
        return self._request_session("broadcast_tx_async", params=tx_data)

    def _broadcast_tx_commit(self, tx_data: Dict):
        """CONTRACT: only returns error if mempool.CheckTx() errs or if we timeout waiting for tx to commit.
        """
        return self._request_session("broadcast_tx_commit", params=tx_data)

    def _broadcast_tx_sync(self, tx_data: Dict):
        """Returns with the response from CheckTx.
        """
        return self._request_session("broadcast_tx_sync", params=tx_data)

    def get_consensus_params(self, height: Optional[int] = None):
        """Get the consensus parameters at the given block height. If no height is provided, it will fetch the
        current consensus params.

        height: int

        """
        data = {
            'height': str(height) if height else None
        }

        return self._request('consensus_params', data=data)

    def get_tx(self, tx_hash: str, prove: Optional[bool] = None):
        """Tx allows you to query the transaction results. nil could mean the transaction is in the mempool,
        invalidated, or was not sent in the first place.

        tx_hash	string	""	true	Query
        prove	bool	false	false	Include proofs of the transactions inclusion in the block

        """

        data = {
            'hash': tx_hash
        }
        if prove:
            data['prove'] = str(prove)

        return self._request('tx', data=data)

    def tx_search(self, query: str, prove: Optional[bool] = None,
                  page: Optional[int] = None, limit: Optional[int] = None):
        """TxSearch allows you to query for multiple transactions results. It returns a list of transactions
        (maximum ?per_page entries) and the total count.

        query	string	""	true	Query
        prove	bool	false	false	Include proofs of the transactions inclusion in the block
        page	int	1	false	Page number (1-based)
        per_page	int	30	false	Number of entries per page (max: 100)

        """

        data = {
            'query': query
        }
        if prove:
            data['prove'] = str(prove)
        if page:
            data['page'] = str(page)
        if limit:
            data['limit'] = str(limit)

        return self._request('tx_search', data=data)


class AsyncHttpRpcClient(BaseHttpRpcClient):
    DEFAULT_TIMEOUT = 10

    @classmethod
    async def create(cls, endpoint_url):

        return AsyncHttpRpcClient(endpoint_url)

    def _init_session(self, **kwargs):

        loop = kwargs.get('loop', asyncio.get_event_loop())
        session = aiohttp.ClientSession(
            loop=loop,
            headers=_get_headers(),
            json_serialize=ujson.dumps
        )
        return session

    async def _request(self, path, **kwargs):

        rpc_request = self._get_rpc_request(path, **kwargs)

        response = await self.session.post(self._endpoint_url, data=rpc_request.encode(), headers=_get_headers())
        return await self._handle_response(response)

    async def _request_session(self, path, params=None):

        kwargs = {
            'params': params,
            'headers': _get_headers()
        }

        response = await self.session.get(f"{self._endpoint_url}/{path}", **kwargs)

        return await self._handle_session_response(response)

    async def _handle_response(self, response):
        """Raises the appropriate exceptions when necessary; otherwise, returns the response.
        """

        try:
            res = await response.json()

            if 'error' in res and res['error']:
                raise Exception(response)

            # by default return full response
            # if it's a normal response we have a data attribute, return that
            if 'result' in res:
                res = res['result']
            return res
        except ValueError:
            raise Exception('Invalid Response: %s' % response.text)

    async def _handle_session_response(self, response):
        """Raises the appropriate exceptions when necessary; otherwise, returns the response.
        """
        if not str(response.status).startswith('2'):
            raise Exception(response)
        try:
            res = await response.json()

            if 'code' in res and res['code'] != "200000":
                raise Exception(response)

            if 'success' in res and not res['success']:
                raise Exception(response)

            # by default return full response
            # if it's a normal response we have a data attribute, return that
            if 'result' in res:
                res = res['result']
            return res
        except ValueError:
            raise Exception('Invalid Response: %s' % await response.text())

    async def get_path_list(self):
        res = await self.client.session.get(self._endpoint_url)
        return await res.text()

    get_path_list.__doc__ = HttpRpcClient.get_path_list.__doc__

    async def get_abci_info(self):
        return await self._request('abci_info')

    get_abci_info.__doc__ = HttpRpcClient.get_abci_info.__doc__

    async def get_consensus_state(self):
        return await self._request('consensus_state')

    get_consensus_state.__doc__ = HttpRpcClient.get_consensus_state.__doc__

    async def dump_consensus_state(self):
        return await self._request('dump_consensus_state')

    dump_consensus_state.__doc__ = HttpRpcClient.dump_consensus_state.__doc__

    async def get_genesis(self):
        return await self._request('genesis')

    get_genesis.__doc__ = HttpRpcClient.get_genesis.__doc__

    async def get_net_info(self):
        return await self._request('net_info')

    get_net_info.__doc__ = HttpRpcClient.get_net_info.__doc__

    async def get_num_unconfirmed_txs(self):
        return await self._request('num_unconfirmed_txs')

    get_num_unconfirmed_txs.__doc__ = HttpRpcClient.get_num_unconfirmed_txs.__doc__

    async def get_status(self):
        return await self._request('status')

    get_status.__doc__ = HttpRpcClient.get_status.__doc__

    async def get_health(self):
        return await self._request('health')

    get_health.__doc__ = HttpRpcClient.get_health.__doc__

    async def get_unconfirmed_txs(self):
        data = {
            'limit': str('100'),
        }
        return await self._request('unconfirmed_txs', data=data)

    get_unconfirmed_txs.__doc__ = HttpRpcClient.get_unconfirmed_txs.__doc__

    async def get_validators(self, height: int, page: int = 1):
        data = {
            'height': str(height),
            'page': str(page),
            'per_page': '10'
        }
        return await self._request('validators', data=data)

    get_validators.__doc__ = HttpRpcClient.get_validators.__doc__

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

        return await self._request('abci_query', data=data)

    abci_query.__doc__ = HttpRpcClient.abci_query.__doc__

    async def get_block(self, height: Optional[int] = None):
        data = {
            'height': str(height) if height else None
        }
        return await self._request('block', data=data)

    get_block.__doc__ = HttpRpcClient.get_block.__doc__

    async def get_block_results(self, height: int):
        data = {
            'height': str(height)
        }
        return await self._request('block_result', data=data)

    get_block_results.__doc__ = HttpRpcClient.get_block_results.__doc__

    async def get_block_commit(self, height: int):
        data = {
            'height': str(height)
        }
        return await self._request('commit', data=data)

    get_block_commit.__doc__ = HttpRpcClient.get_block_commit.__doc__

    async def get_blockchain_info(self, min_height: int, max_height: int):
        assert max_height > min_height

        data = {
            'minHeight': str(min_height),
            'maxHeight': str(max_height)
        }

        return await self._request('blockchain', data=data)

    get_blockchain_info.__doc__ = HttpRpcClient.get_blockchain_info.__doc__

    async def _broadcast_tx_async(self, tx_data: Dict):
        """Returns right away, with no response
        """
        return await self._request_session('broadcast_tx_async', params=tx_data)

    _broadcast_tx_async.__doc__ = HttpRpcClient._broadcast_tx_async.__doc__

    async def _broadcast_tx_commit(self, tx_data: Dict):
        return await self._request_session('broadcast_tx_commit', params=tx_data)

    _broadcast_tx_commit.__doc__ = HttpRpcClient._broadcast_tx_commit.__doc__

    async def _broadcast_tx_sync(self, tx_data: Dict):
        return await self._request_session('broadcast_tx_sync', params=tx_data)

    _broadcast_tx_sync.__doc__ = HttpRpcClient._broadcast_tx_sync.__doc__

    async def get_consensus_params(self, height: Optional[int] = None):
        data = {
            'height': str(height) if height else None
        }

        return await self._request('consensus_params', data=data)

    get_consensus_params.__doc__ = HttpRpcClient.get_consensus_params.__doc__

    async def get_tx(self, tx_hash: str, prove: Optional[bool] = None):
        data = {
            'hash': tx_hash
        }
        if prove:
            data['prove'] = str(prove)

        return await self._request('tx', data=data)

    get_tx.__doc__ = HttpRpcClient.get_tx.__doc__

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

        return await self._request('tx_search', data=data)

    tx_search.__doc__ = HttpRpcClient.tx_search.__doc__
