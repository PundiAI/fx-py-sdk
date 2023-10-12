import unittest

from google.protobuf.json_format import MessageToJson

from fxsdk.client.crosschain import CrossChainClient, CrossChainTarget
from fxsdk.msg import new_msg_send
from fxsdk.wallet.key import mnemonic_to_privkey
from fxsdk.wallet.builder import TxBuilder
from fxsdk.client.grpc import Client
from fxsdk.x.cosmos.base.v1beta1.coin_pb2 import Coin
from fxsdk.x.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_SYNC

grpc_url = 'localhost:9090'
address_prefix = 'mx'
private_key = mnemonic_to_privkey("test test test test test test test test test test test junk")
tx_builder = TxBuilder(private_key=private_key, prefix=address_prefix)


class TestSendTx(unittest.TestCase):

    def test_bank_send(self):
        from_addr = tx_builder.from_address().to_string()
        send_msg_any = new_msg_send(
            from_address=from_addr,
            to_address=from_addr,
            amount=[Coin(amount='100', denom='cusd')],
        )

        grpc_cli = Client(grpc_url)
        tx = grpc_cli.build_tx(tx_builder, [send_msg_any])
        print(MessageToJson(tx))

        tx_response = grpc_cli.broadcast_tx(tx, BROADCAST_MODE_SYNC)
        print(tx_response)
        self.assertEqual(tx_response.code, 0)

        tx_response = grpc_cli.wait_mint_tx(tx_response.txhash)
        print(tx_response)

    def test_ibc_transfer_mx2eth(self):
        grpc_cli = CrossChainClient(grpc_url)
        channels = grpc_cli.query_channels()
        if len(channels) == 0:
            print("no channel found")
            return
        channel = channels[0].channel_id
        to_address = tx_builder.from_address().to_hex()
        amount = Coin(denom='FX', amount='100')
        tx_response = grpc_cli.ibc_transfer(tx_builder=tx_builder, to_address=to_address, amount=amount,
                                            channel=channel, target=CrossChainTarget.Ethereum,
                                            mode=BROADCAST_MODE_SYNC)
        print(tx_response)
        self.assertEqual(tx_response.code, 0)

    def test_ibc_transfer_mx2mx(self):
        grpc_cli = CrossChainClient(grpc_url)
        channels = grpc_cli.query_channels()
        if len(channels) == 0:
            print("no channel found")
            return
        from_channel = channels[0].channel_id
        to_channel = "channel-6"
        amount = Coin(denom='FX', amount='100')
        tx_response = grpc_cli.ibc_transfer_mx2mx(tx_builder=tx_builder, amount=amount, from_channel=from_channel,
                                                  to_channel=to_channel, mode=BROADCAST_MODE_SYNC)
        print(tx_response)
        self.assertEqual(tx_response.code, 0)


if __name__ == '__main__':
    unittest.main()
