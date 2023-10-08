import unittest

from google.protobuf.any_pb2 import Any
from google.protobuf.json_format import MessageToJson

from fxsdk.wallet.key import mnemonic_to_privkey
from fxsdk.wallet.builder import TxBuilder
from fxsdk.client.grpc_client import BaseClient
from fxsdk.x.cosmos.bank.v1beta1.tx_pb2 import MsgSend
from fxsdk.x.cosmos.base.v1beta1.coin_pb2 import Coin
from fxsdk.x.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_SYNC


class TestGrpcSendTx(unittest.TestCase):

    def test_send_tx(self):
        private_key = mnemonic_to_privkey(
            "test test test test test test test test test test test junk")

        from_addr = private_key.to_address()
        print('address:', from_addr)

        cli = BaseClient('127.0.0.1:9090')

        send_msg = MsgSend(from_address=from_addr, to_address=from_addr,
                           amount=[Coin(amount='100', denom='FX')])
        send_msg_any = Any(type_url='/cosmos.bank.v1beta1.MsgSend',
                           value=send_msg.SerializeToString())

        tx_builder = TxBuilder(private_key)

        tx = cli.build_tx(tx_builder, [send_msg_any])
        print(MessageToJson(tx))

        tx_response = cli.broadcast_tx(tx, BROADCAST_MODE_SYNC)
        print(tx_response)

        self.assertEqual(tx_response.code, 0)

        tx_response = cli.wait_mint_tx(tx_response.txhash)
        print(tx_response)


if __name__ == '__main__':
    unittest.main()
