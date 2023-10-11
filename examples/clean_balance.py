from google.protobuf.any_pb2 import Any

from fxsdk.client.grpc import Client
from fxsdk.wallet.builder import TxBuilder
from fxsdk.wallet.key import PrivateKey
from fxsdk.wallet.key import mnemonic_to_privkey
from fxsdk.x.cosmos.bank.v1beta1.tx_pb2 import MsgSend
from fxsdk.x.cosmos.base.v1beta1.coin_pb2 import Coin
from fxsdk.x.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_SYNC


def clean_balance(grpc_client: Client, from_private_key: PrivateKey, to_addr: str) -> str:
    from_addr = from_private_key.to_address()

    gas_price = Coin(amount='4000000000000', denom='FX')
    gas_limit = 200000
    fee_amount = gas_limit * int(gas_price.amount)

    balance = grpc_client.query_balance(from_addr, "FX")
    if int(balance.amount) <= fee_amount:
        raise Exception('Insufficient account balance: ' + from_addr)

    send_amount = int(balance.amount) - fee_amount

    send_msg = MsgSend(from_address=from_addr, to_address=to_addr,
                       amount=[Coin(amount=str(send_amount), denom='FX')])
    send_msg_any = Any(type_url='/cosmos.bank.v1beta1.MsgSend',
                       value=send_msg.SerializeToString())

    tx_builder = TxBuilder(private_key=from_private_key, gas_price=gas_price)

    tx = grpc_client.build_tx(tx_builder, [send_msg_any], gas_limit=gas_limit)
    # print(MessageToJson(tx))

    tx_response = grpc_client.broadcast_tx(tx, BROADCAST_MODE_SYNC)
    if tx_response.code != 0:
        raise Exception("broadcast tx failed, txhash: ", tx_response.txhash)
    tx_response = grpc_client.wait_mint_tx(tx_response.txhash)
    return tx_response.txhash


if __name__ == '__main__':

    cli = Client('127.0.0.1:9090')

    a_private_key = mnemonic_to_privkey(
        "test test test test test test test test test test test junk")
    a_addr = a_private_key.to_address()
    a_balance = cli.query_balance(a_addr, 'FX')

    b_private_key = mnemonic_to_privkey(
        "test test test test test test test test test test test junk")
    b_addr = b_private_key.to_address()
    b_balance = cli.query_balance(b_addr, 'FX')

    if int(a_balance.amount) >= int(b_balance.amount):

        txHash = clean_balance(cli, a_private_key, b_addr)
        print("txHash(a=>b)", txHash)
    else:

        txHash = clean_balance(cli, b_private_key, a_addr)
        print("txHash(b=>a)", txHash)

    a_balance = cli.query_balance(a_addr, 'FX')

    b_balance = cli.query_balance(b_addr, 'FX')
