import unittest

from fxsdk.client.http import HttpRpcClient, AsyncHttpRpcClient

rpc_url = "http://127.0.0.1:26657"
rpc_client = HttpRpcClient(rpc_url)


class TestHttpRpcClient(unittest.TestCase):

    def test_get_block_result(self):
        block_res = rpc_client.get_block_results(1)
        print(block_res)
        assert block_res


class TestAsyncHttpRpcClient(unittest.IsolatedAsyncioTestCase):
    async def test_get_block_result(self):
        rcp_client = await AsyncHttpRpcClient.create(rpc_url)
        block_results = await rcp_client.get_block_results(1)
        print(block_results)


if __name__ == '__main__':
    unittest.main()
