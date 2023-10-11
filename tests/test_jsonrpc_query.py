import unittest

from fxsdk.client.jsonrpc import JsonRpcClient

rpc_client = JsonRpcClient("http://127.0.0.1:26657")


class TestJsonRpcCase(unittest.TestCase):

    def test_get_block_result(self):
        block_res = rpc_client.get_block_results(1)
        print(block_res)
        assert block_res


if __name__ == '__main__':
    unittest.main()
