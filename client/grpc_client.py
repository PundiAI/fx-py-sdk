import time
import grpc

from google.protobuf.any_pb2 import Any
from urllib.parse import urlparse
from typing import Optional

from wallet.builder import TxBuilder
from x.cosmos.auth.v1beta1.auth_pb2 import BaseAccount
from x.cosmos.auth.v1beta1.query_pb2 import QueryAccountRequest
from x.cosmos.auth.v1beta1.query_pb2_grpc import QueryStub as AuthQuery
from x.cosmos.bank.v1beta1.bank_pb2 import Supply
from x.cosmos.bank.v1beta1.query_pb2 import QueryBalanceRequest, QueryAllBalancesRequest, QueryTotalSupplyRequest
from x.cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankQuery
from x.cosmos.base.abci.v1beta1.abci_pb2 import GasInfo, TxResponse
from x.cosmos.base.tendermint.v1beta1.query_pb2 import GetBlockByHeightRequest, GetLatestBlockRequest, \
    GetSyncingRequest, GetNodeInfoRequest
from x.cosmos.base.tendermint.v1beta1.query_pb2_grpc import ServiceStub as TendermintClient
from x.cosmos.base.v1beta1.coin_pb2 import Coin
from x.cosmos.staking.v1beta1.query_pb2 import QueryValidatorsRequest
from x.cosmos.staking.v1beta1.query_pb2_grpc import QueryStub as StakingClient
from x.cosmos.staking.v1beta1.staking_pb2 import Validator
from x.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_BLOCK, BroadcastMode, BroadcastTxRequest, SimulateRequest, \
    GetTxRequest, GetTxResponse
from x.cosmos.tx.v1beta1.service_pb2_grpc import ServiceStub as TxClient
from x.cosmos.tx.v1beta1.tx_pb2 import Fee, Tx, TxRaw
from x.cosmos.base.node.v1beta1.query_pb2_grpc import ServiceStub as CosmosNodeClient
from x.cosmos.base.node.v1beta1.query_pb2 import ConfigRequest
from x.tendermint.p2p.types_pb2 import DefaultNodeInfo
from x.tendermint.types.block_pb2 import Block

GRPCBlockHeightHeader = 'x-cosmos-block-height'


class BaseClient:
    def __init__(self, url: str = 'localhost:9090'):
        if urlparse(url).scheme == "https":
            self.channel = grpc.secure_channel(
                urlparse(url).netloc, grpc.ssl_channel_credentials())
        else:
            self.channel = grpc.insecure_channel(url)

    def query_account_info(self, address: str, height: Optional[int] = 0) -> BaseAccount:

        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = AuthQuery(self.channel).Account(QueryAccountRequest(address=address), metadata=metadata)
        account_any = response.account
        account = BaseAccount()
        if account_any.Is(account.DESCRIPTOR):
            account_any.Unpack(account)
            return account

    def query_all_balances(self, address: str, height: Optional[int] = 0) -> [Coin]:

        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = BankQuery(self.channel).AllBalances(QueryAllBalancesRequest(address=address), metadata=metadata)
        return response.balances

    def query_balance(self, address: str, denom: str, height: Optional[int] = 0) -> Coin:

        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = BankQuery(self.channel).Balance(QueryBalanceRequest(address=address, denom=denom), metadata=metadata)
        return response.balance

    def query_total_supply(self, height: Optional[int] = 0) -> [Supply]:

        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = BankQuery(self.channel).TotalSupply(QueryTotalSupplyRequest(), metadata=metadata)
        return response.supply

    def query_gas_price(self, height: Optional[int] = 0) -> [Coin]:

        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = CosmosNodeClient(self.channel).Config(ConfigRequest(), metadata=metadata)
        return response.minimum_gas_price

    def query_block_by_height(self, height: int) -> Block:

        response = TendermintClient(self.channel).GetBlockByHeight(GetBlockByHeightRequest(height))
        return response.block

    def query_latest_block(self) -> Block:

        response = TendermintClient(self.channel).GetLatestBlock(GetLatestBlockRequest())
        return response.block

    def query_chain_id(self) -> str:

        response = TendermintClient(self.channel).GetLatestBlock(GetLatestBlockRequest())
        return response.block.header.chain_id

    def query_node_syncing(self) -> bool:

        response = TendermintClient(self.channel).GetSyncing(GetSyncingRequest())
        return response.syncing

    def query_node_info(self) -> DefaultNodeInfo:

        response = TendermintClient(self.channel).GetNodeInfo(GetNodeInfoRequest())
        return response.default_node_info

    def query_validator_list(self, height: Optional[int] = 0) -> [Validator]:

        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = StakingClient(self.channel).Validators(QueryValidatorsRequest(), metadata=metadata)
        return response.validators

    def query_tx(self, tx_hash: str) -> GetTxResponse:

        return TxClient(self.channel).GetTx(GetTxRequest(hash=tx_hash))

    def build_tx(self, tx_builder: TxBuilder, msg: [Any], account_number: int = -1,
                 sequence: int = -1, gas_limit: int = 0) -> Tx:

        if tx_builder.chain_id == '':
            tx_builder.chain_id = self.query_chain_id()

        if account_number < 0 or sequence < 0:
            account = self.query_account_info(tx_builder.address())
            account_number = account.account_number
            sequence = account.sequence

        gas_price_amount = int(tx_builder.gas_price.amount)
        fee_denom = tx_builder.gas_price.denom
        if gas_price_amount <= 0:

            for item in self.query_gas_price():
                if item.denom == fee_denom:
                    gas_price_amount = int(item.amount)

        if gas_limit <= 0:
            gas_limit = 500_000
            fee_amount = Coin(amount=str(
                gas_limit * gas_price_amount), denom=fee_denom)
            fee = Fee(amount=[fee_amount], gas_limit=gas_limit)
            tx = tx_builder.sign(msg, fee, account_number, sequence)

            gas_info = self.estimating_gas(tx)
            gas_limit = int(float(gas_info.gas_used) * 1.5)

        fee_amount = Coin(amount=str(
            gas_limit * gas_price_amount), denom=fee_denom)
        fee = Fee(amount=[fee_amount], gas_limit=gas_limit)
        return tx_builder.sign(msg, fee, account_number, sequence)

    def estimating_gas(self, tx: Tx) -> GasInfo:

        response = TxClient(self.channel).Simulate(SimulateRequest(tx=tx))
        return response.gas_info

    def broadcast_tx(self, tx: Tx, mode: BroadcastMode = BROADCAST_MODE_BLOCK) -> TxResponse:

        tx_raw = TxRaw(body_bytes=tx.body.SerializeToString(),
                       auth_info_bytes=tx.auth_info.SerializeToString(),
                       signatures=tx.signatures)
        tx_bytes = tx_raw.SerializeToString()
        response = TxClient(self.channel).BroadcastTx(
            BroadcastTxRequest(tx_bytes=tx_bytes, mode=mode))
        return response.tx_response

    def wait_mint_tx(self, tx_hash: str) -> TxResponse:

        for i in range(5):
            time.sleep(5)
            try:
                response = self.query_tx(tx_hash)
                return response.tx_response
            except:
                continue
        raise Exception("not found tx")
