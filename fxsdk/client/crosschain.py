from enum import Enum
from typing import Optional

import requests
from eth_utils import is_hex_address

from fxsdk.client.grpc import Client, GRPCBlockHeightHeader
from fxsdk.msg import new_ibc_fx_msg_transfer
from fxsdk.wallet.builder import TxBuilder
from fxsdk.x.cosmos.base.v1beta1.coin_pb2 import Coin
from fxsdk.x.cosmos.tx.v1beta1.service_pb2 import BroadcastMode, BROADCAST_MODE_UNSPECIFIED
from fxsdk.x.ibc.core.channel.v1.channel_pb2 import Channel, IdentifiedChannel
from fxsdk.x.ibc.core.channel.v1.query_pb2 import QueryChannelRequest, QueryChannelsRequest
from fxsdk.x.ibc.core.channel.v1.query_pb2_grpc import QueryStub as IbcChannelClient


class CrossChainTarget(Enum):
    Ethereum = 'ethereum'
    MarginX = 'marginx'
    FxCore = 'fxcore'


bridge_fee_api = "https://starscan.io/explorer/gravity/v2/fee/search"


class BridgeFee:

    def __init__(self, url: str = bridge_fee_api):
        self._url = url

    def _get_api(self, chain_id: str, denom: str) -> str:
        if denom == 'FX':
            token_contract = '0x8c15ef5b4b21951d50e53e4fbda8298ffad25057'
        elif denom == 'USDT':
            token_contract = '0xdac17f958d2ee523a2206206994597c13d831ec7'
        else:
            raise Exception("denom not supported")
        api = '{}?chainId={}&tokenContract={}'.format(self._url, chain_id, token_contract)
        return api

    def get_fast(self, chain_id: str, denom: str) -> int:
        result = requests.get(self._get_api(chain_id, denom))
        return result.json()['data']['rapid']

    def get_standard(self, chain_id: str, denom: str) -> int:
        result = requests.get(self._get_api(chain_id, denom))
        return result.json()['data']['standard']


class CrossChainClient(Client, BridgeFee):

    def __init__(self, url: str = 'localhost:9090'):
        super().__init__(url)
        BridgeFee.__init__(self)

    def query_channel(self, channel_id: str, height: Optional[int] = 0) -> Channel:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = IbcChannelClient(self.channel).Channel(
            QueryChannelRequest(port_id='transfer', channel_id=channel_id), metadata=metadata)
        return response.channel

    def query_channels(self, height: Optional[int] = 0) -> [IdentifiedChannel]:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = IbcChannelClient(self.channel).Channels(QueryChannelsRequest(), metadata=metadata)
        return response.channels

    def ibc_transfer(self, tx_builder: TxBuilder, to_address: str, amount: Coin, channel: str, target: CrossChainTarget,
                     mode: Optional[BroadcastMode] = BROADCAST_MODE_UNSPECIFIED):
        router = ''
        fee = Coin(denom=amount.denom, amount='0')
        if target is CrossChainTarget.Ethereum:
            router = 'eth'
            fee.amount = self.get_fast(target.value, amount.denom)
        elif target is CrossChainTarget.MarginX:
            pass
        elif target is CrossChainTarget.FxCore:
            if is_hex_address(to_address) is False:
                raise Exception("address should be hex format")
        else:
            raise Exception("target chain not supported")
        sender = tx_builder.from_address().to_string()
        msg = new_ibc_fx_msg_transfer(channel=channel, sender=sender, receiver=to_address, token=amount,
                                      router=router, fee=fee)
        if mode is BROADCAST_MODE_UNSPECIFIED or mode is None:
            return self.build_tx(tx_builder=tx_builder, msgs=[msg])
        else:
            return self.build_and_broadcast_tx(tx_builder=tx_builder, msgs=[msg], mode=mode)

    def ibc_transfer_mx2mx(self, tx_builder: TxBuilder, amount: Coin, from_channel: str, to_channel: str,
                           mode: Optional[BroadcastMode] = BROADCAST_MODE_UNSPECIFIED):
        address = tx_builder.from_address()
        to_address = "{}|transfer/{}:{}".format(address.to_string("fx"), to_channel, address.to_string())
        self.ibc_transfer(tx_builder=tx_builder, to_address=to_address, amount=amount, channel=from_channel,
                          target=CrossChainTarget.MarginX, mode=mode)
