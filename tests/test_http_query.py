import asyncio
import logging.config
import unittest
from typing import Dict

import yaml

from fxsdk.client.http import HttpRpcClient, AsyncHttpRpcClient
from fxsdk.client.websockets import WebsocketRpcClient

rpc_url = "http://127.0.0.1:26657"
rpc_client = HttpRpcClient(rpc_url)


class TestHttpRpcClient(unittest.TestCase):

    def test_get_block_result(self):
        block_res = rpc_client.get_block_results(1)
        print(block_res)
        assert block_res


class TestWebsocketRpcClient(unittest.IsolatedAsyncioTestCase):

    @staticmethod
    async def callback(msg: Dict):
        print("-------------", msg)

    async def test_get_block_result(self):
        logging.config.dictConfig(yaml.safe_load(open('../.logging.yaml', 'r')))
        ws_client = await WebsocketRpcClient.create(endpoint_url=rpc_url, callback=self.callback)
        await ws_client.get_status()
        await ws_client.subscribe("tm.event='NewBlock'")
        await asyncio.sleep(10)
        ws_client.close()


class TestAsyncHttpRpcClient(unittest.IsolatedAsyncioTestCase):
    async def test_get_block_result(self):
        rcp_client = await AsyncHttpRpcClient.create(rpc_url)
        block_results = await rcp_client.get_block_results(1)
        print(block_results)


if __name__ == '__main__':
    unittest.main()
