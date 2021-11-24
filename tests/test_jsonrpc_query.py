import unittest

from jsonrpc.client import *

rpc_client = HttpRpcClient("http://127.0.0.1:26657")


class MyTestCase(unittest.TestCase):

    @staticmethod
    def test_rpc_client():
        abci_info = rpc_client.get_abci_info()
        print("abci_info:", abci_info)
        assert rpc_client.get_abci_info()

        consensus_state = rpc_client.dump_consensus_state()
        print("consensus_state: ", consensus_state)
        assert rpc_client.dump_consensus_state()

        net_info = rpc_client.get_net_info()
        print("net_info: ", net_info)
        assert rpc_client.get_net_info()

        num_unconfirmed_txs = rpc_client.get_num_unconfirmed_txs()
        print("num_unconfirmed_txs: ", num_unconfirmed_txs)
        assert rpc_client.get_num_unconfirmed_txs()

        status = rpc_client.get_status()
        print("status: ", status)
        assert rpc_client.get_status()

        validators = rpc_client.get_validators(1)
        print("validators: ", validators)
        assert rpc_client.get_validators(1)

        unconfirmed_txs = rpc_client.get_unconfirmed_txs()
        print("unconfirmed_txs: ", unconfirmed_txs)
        assert rpc_client.get_unconfirmed_txs()

        genesis = rpc_client.get_genesis()
        print(genesis)
        assert rpc_client.get_genesis()

    @staticmethod
    def test_get_block_result():
        block_res = rpc_client.get_block_results(1)
        print(block_res)
        assert block_res


if __name__ == '__main__':
    unittest.main()
