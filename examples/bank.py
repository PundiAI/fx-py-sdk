from fxsdk.client.grpc_client import Client
from fxsdk.wallet.builder import TxBuilder
from fxsdk.x.cosmos.base.v1beta1.coin_pb2 import Coin

if __name__ == '__main__':
    url = '127.0.0.1:9090'
    grpc_cli = Client(url=url)

    mnemonic = 'test test test test test test test test test test test junk'
    prefix = 'mx'
    tx_builder = TxBuilder.from_mnemonic(mnemonic=mnemonic, prefix=prefix)

    to = tx_builder.address()
    amount = [Coin(amount='100', denom='cusd')]
    tx_response = grpc_cli.bank_send(tx_builder, to, amount)
    print(tx_response)
