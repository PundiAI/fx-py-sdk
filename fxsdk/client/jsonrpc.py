import itertools
import json
import traceback
import requests
import ujson

from typing import Optional, Dict
from requests.sessions import ChunkedEncodingError, HTTPAdapter
from urllib3.util.retry import Retry
from collections import OrderedDict

requests.models.json = ujson


def _get_headers():
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }


class Base:
    id_generator = itertools.count(1)

    def __init__(self, endpoint_url, requests_params: Optional[Dict] = None):
        self._endpoint_url = endpoint_url
        self._requests_params = requests_params

        self.session = self._init_session()

    @staticmethod
    def _init_session():
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


class JsonRpcClient(Base):

    def __init__(self, endpoint_url, requests_params: Optional[Dict] = None, max_retries=3):
        super(JsonRpcClient, self).__init__(endpoint_url, requests_params)
        if max_retries:
            retries = Retry(total=max_retries,
                            backoff_factor=.5,
                            status_forcelist=[500, 502, 503, 504])
            self.session.mount('http://', HTTPAdapter(max_retries=retries))

    def _request(self, path, **kwargs):
        rpc_request = self._get_rpc_request(path, **kwargs)
        try:
            response = self.session.post(self._endpoint_url, data=rpc_request.encode(), headers=_get_headers())
            return self._handle_response(response)
        except ChunkedEncodingError:
            print(f'Error getting {json.loads(rpc_request)["params"]["height"]}')
            traceback.print_exc()

    def _request_session(self, path, params=None):
        kwargs = {
            'params': params,
            'headers': _get_headers()
        }

        response = self.session.get(f"{self._endpoint_url}/{path}", **kwargs)

        return self._handle_session_response(response)

    @staticmethod
    def _handle_response(response):
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
        res = self._request(self._endpoint_url, method="get")
        return res.content

    def get_abci_info(self):
        return self._request('abci_info')

    def get_consensus_state(self):
        return self._request('consensus_state')

    def get_genesis(self):
        return self._request('genesis')

    def get_net_info(self):
        return self._request('net_info')

    def get_num_unconfirmed_txs(self):
        return self._request('num_unconfirmed_txs')

    def get_status(self):
        return self._request('status')

    def get_health(self):
        return self._request('health')

    def get_validators(self, height: int, page: int = 1):
        data = {
            'height': str(height),
            'page': str(page),
            'per_page': '10'
        }
        return self._request('validators', data=data)

    def get_consensus_params(self, height: Optional[int] = None):
        data = {
            'height': str(height) if height else None
        }

        return self._request('consensus_params', data=data)

    def abci_query(self, data: str,
                   path: Optional[str] = None,
                   prove: Optional[bool] = None,
                   height: Optional[int] = None):
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
        data = {
            'height': str(height) if height else None
        }

        return self._request('block', data=data)

    def get_block_results(self, height: int):
        data = {
            'height': str(height)
        }

        return self._request('block_results', data=data)

    def get_block_commit(self, height: int):
        data = {
            'height': str(height)
        }

        return self._request('commit', data=data)

    def get_blockchain_info(self, min_height: int, max_height: int):
        assert max_height > min_height

        data = {
            'minHeight': str(min_height),
            'maxHeight': str(max_height)
        }

        return self._request('blockchain', data=data)

    def _broadcast_tx_async(self, tx_data: Dict):
        return self._request_session("broadcast_tx_async", params=tx_data)

    def _broadcast_tx_commit(self, tx_data: Dict):
        return self._request_session("broadcast_tx_commit", params=tx_data)

    def _broadcast_tx_sync(self, tx_data: Dict):
        return self._request_session("broadcast_tx_sync", params=tx_data)

    def get_tx(self, tx_hash: str, prove: Optional[bool] = None):
        data = {
            'hash': tx_hash
        }
        if prove:
            data['prove'] = str(prove)

        return self._request('tx', data=data)

    def tx_search(self, query: str, prove: Optional[bool] = None,
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

        return self._request('tx_search', data=data)


class RpcRequest:

    def __init__(self, method, req_id, params=None):
        self._method = method
        self._params = params
        self._id = req_id

    @staticmethod
    def _sort_request(request):
        sort_order = ["jsonrpc", "method", "params", "id"]
        return OrderedDict(sorted(request.items(), key=lambda k: sort_order.index(k[0])))

    def __str__(self):
        request = {
            'jsonrpc': '2.0',
            'method': self._method,
            'id': self._id
        }

        if self._params:
            request['params'] = self._params

        return ujson.dumps(self._sort_request(request), ensure_ascii=False)
