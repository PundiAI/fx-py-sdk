import unittest

from jsonrpc.client import *

rpc_client = HttpRpcClient("http://127.0.0.1:26657")


class MyTestCase(unittest.TestCase):

    @staticmethod
    def test_get_block_result():
        block_res = rpc_client.get_block_results(1)
        print(block_res)
        assert block_res


if __name__ == '__main__':
    unittest.main()
