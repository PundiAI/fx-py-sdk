import unittest

from google.protobuf.json_format import MessageToJson

from fxsdk.msg import new_msg_send
from fxsdk.wallet.key import mnemonic_to_privkey
from fxsdk.wallet.builder import TxBuilder
from fxsdk.client.grpc_client import Client
from fxsdk.x.cosmos.base.v1beta1.coin_pb2 import Coin
from fxsdk.x.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_SYNC

grpc_cli = Client('localhost:9090')


class TestGrpcSendTx(unittest.TestCase):

    def test_bank_send(self):
        address_prefix = 'mx'
        private_key = mnemonic_to_privkey("test test test test test test test test test test test junk")

        from_addr = private_key.to_address(address_prefix)
        print('address:', from_addr)

        send_msg_any = new_msg_send(from_address=from_addr, to_address=from_addr,
                                    amount=[Coin(amount='100', denom='cusd')])

        tx_builder = TxBuilder(private_key=private_key, prefix=address_prefix)

        tx = grpc_cli.build_tx(tx_builder, [send_msg_any])
        print(MessageToJson(tx))

        tx_response = grpc_cli.broadcast_tx(tx, BROADCAST_MODE_SYNC)
        print(tx_response)

        self.assertEqual(tx_response.code, 0)

        tx_response = grpc_cli.wait_mint_tx(tx_response.txhash)
        print(tx_response)


if __name__ == '__main__':
    unittest.main()
