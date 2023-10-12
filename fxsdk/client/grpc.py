import time
import grpc

from google.protobuf.any_pb2 import Any
from urllib.parse import urlparse
from typing import Optional

from fxsdk.msg import new_msg_send
from fxsdk.wallet.builder import TxBuilder
from fxsdk.coin import parse_coins

from fxsdk.x.cosmos.auth.v1beta1.auth_pb2 import BaseAccount, ModuleAccount
from fxsdk.x.cosmos.auth.v1beta1.query_pb2 import QueryAccountRequest, Bech32PrefixRequest, QueryModuleAccountsRequest
from fxsdk.x.cosmos.auth.v1beta1.query_pb2_grpc import QueryStub as AuthClient
from fxsdk.x.cosmos.bank.v1beta1.bank_pb2 import Supply
from fxsdk.x.cosmos.bank.v1beta1.query_pb2 import (QueryBalanceRequest, QueryAllBalancesRequest,
                                                   QueryTotalSupplyRequest, QuerySupplyOfRequest)
from fxsdk.x.cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankClient
from fxsdk.x.cosmos.base.abci.v1beta1.abci_pb2 import GasInfo, TxResponse
from fxsdk.x.cosmos.base.tendermint.v1beta1.query_pb2 import GetBlockByHeightRequest, GetLatestBlockRequest, \
    GetSyncingRequest, GetNodeInfoRequest
from fxsdk.x.cosmos.base.tendermint.v1beta1.query_pb2_grpc import ServiceStub as TendermintClient
from fxsdk.x.cosmos.base.v1beta1.coin_pb2 import Coin
from fxsdk.x.cosmos.staking.v1beta1.query_pb2 import QueryValidatorsRequest
from fxsdk.x.cosmos.staking.v1beta1.query_pb2 import QueryParamsRequest as QueryStakingParamsRequest
from fxsdk.x.cosmos.staking.v1beta1.query_pb2_grpc import QueryStub as StakingClient
from fxsdk.x.cosmos.staking.v1beta1.staking_pb2 import Validator
from fxsdk.x.cosmos.staking.v1beta1.staking_pb2 import Params as StakingParams
from fxsdk.x.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_SYNC, BroadcastMode, BroadcastTxRequest, \
    SimulateRequest, \
    GetTxRequest, GetTxResponse, OrderBy, GetTxsEventRequest, GetTxsEventResponse
from fxsdk.x.cosmos.tx.v1beta1.service_pb2_grpc import ServiceStub as TxClient
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import Fee, Tx, TxRaw
from fxsdk.x.cosmos.base.node.v1beta1.query_pb2_grpc import ServiceStub as CosmosNodeClient
from fxsdk.x.cosmos.base.node.v1beta1.query_pb2 import ConfigRequest
from fxsdk.x.tendermint.p2p.types_pb2 import DefaultNodeInfo
from fxsdk.x.tendermint.types.block_pb2 import Block

GRPCBlockHeightHeader = 'x-cosmos-block-height'
DefGasLimit = 200_000
DefGasAdjustment = 1.5


class Client:
    def __init__(self, url: str = 'localhost:9090'):
        if urlparse(url).scheme == "https":
            self.channel = grpc.secure_channel(
                urlparse(url).netloc, grpc.ssl_channel_credentials())
        else:
            self.channel = grpc.insecure_channel(url)

    def query_account_info(self, address: str, height: Optional[int] = 0) -> BaseAccount:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = AuthClient(self.channel).Account(QueryAccountRequest(address=address), metadata=metadata)
        account_any = response.account
        account = BaseAccount()
        if account_any.Is(account.DESCRIPTOR):
            account_any.Unpack(account)
            return account

    def query_bech32_prefix(self) -> str:
        response = AuthClient(self.channel).Bech32Prefix(Bech32PrefixRequest())
        return response.bech32_prefix

    def query_module_accounts(self) -> [ModuleAccount]:
        response = AuthClient(self.channel).ModuleAccounts(QueryModuleAccountsRequest())
        accounts = []
        for account_any in response.accounts:
            account = ModuleAccount()
            account_any.Unpack(account)
            accounts.append(account)
        return accounts

    def query_all_balances(self, address: str, height: Optional[int] = 0) -> [Coin]:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = BankClient(self.channel).AllBalances(QueryAllBalancesRequest(address=address), metadata=metadata)
        return response.balances

    def query_balance(self, address: str, denom: str, height: Optional[int] = 0) -> Coin:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = BankClient(self.channel).Balance(QueryBalanceRequest(address=address, denom=denom),
                                                    metadata=metadata)
        return response.balance

    def query_total_supply(self, height: Optional[int] = 0) -> [Supply]:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = BankClient(self.channel).TotalSupply(QueryTotalSupplyRequest(), metadata=metadata)
        return response.supply

    def query_supply_of(self, denom: str, height: Optional[int] = 0) -> Coin:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = BankClient(self.channel).SupplyOf(QuerySupplyOfRequest(denom=denom), metadata=metadata)
        return response.amount

    def query_validators(self, height: Optional[int] = 0) -> [Validator]:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = StakingClient(self.channel).Validators(QueryValidatorsRequest(), metadata=metadata)
        return response.validators

    def query_staking_params(self) -> StakingParams:
        response = StakingClient(self.channel).Params(QueryStakingParamsRequest())
        return response.params

    def query_gas_prices(self) -> [Coin]:
        response = CosmosNodeClient(self.channel).Config(ConfigRequest())
        return parse_coins(response.minimum_gas_price)

    def query_block_by_height(self, height: int) -> Block:
        response = TendermintClient(self.channel).GetBlockByHeight(GetBlockByHeightRequest(height))
        return response.block

    def query_latest_block(self) -> Block:
        response = TendermintClient(self.channel).GetLatestBlock(GetLatestBlockRequest())
        return response.block

    def query_chain_id(self) -> str:
        return self.query_node_info().network

    def query_node_syncing(self) -> bool:
        response = TendermintClient(self.channel).GetSyncing(GetSyncingRequest())
        return response.syncing

    def query_node_info(self) -> DefaultNodeInfo:
        response = TendermintClient(self.channel).GetNodeInfo(GetNodeInfoRequest())
        return response.default_node_info

    def query_tx(self, tx_hash: str) -> GetTxResponse:
        return TxClient(self.channel).GetTx(GetTxRequest(hash=tx_hash))

    def query_txs_by_event(self, events, order_by: OrderBy, page: int, limit: int) -> GetTxsEventResponse:
        return TxClient(self.channel).GetTxsEvent(GetTxsEventRequest(
            events=events, order_by=order_by, page=page, limit=limit
        ))

    def bank_send(self, tx_builder: TxBuilder, to: str, amount: [Coin],
                  mode: BroadcastMode = BROADCAST_MODE_SYNC) -> TxResponse:
        from_address = tx_builder.from_address().to_string()
        msg = new_msg_send(from_address=from_address, to_address=to, amount=amount)
        tx = self.build_tx(tx_builder, [msg])
        return self.broadcast_tx(tx, mode)

    def build_tx(self, tx_builder: TxBuilder, msgs: [Any], account_number: int = -1,
                 sequence: int = -1, gas_limit: int = 0) -> Tx:
        if tx_builder.chain_id == '':
            tx_builder.chain_id = self.query_chain_id()

        if account_number < 0 or sequence < 0:
            from_address = tx_builder.from_address().to_string()
            account = self.query_account_info(address=from_address)
            account_number = account.account_number
            sequence = account.sequence

        if tx_builder.has_gas_price() is False:
            gas_prices = self.query_gas_prices()
            tx_builder.with_gas_price(gas_prices)
        gas_fee_denom = tx_builder.gas_price.denom
        gas_price_amount = float(tx_builder.gas_price.amount)

        if gas_limit <= 0:
            gas_limit = DefGasLimit
            fee_amount = Coin(amount=str(int(gas_limit * gas_price_amount)), denom=gas_fee_denom)
            fee = Fee(amount=[fee_amount], gas_limit=gas_limit)
            tx = tx_builder.sign(msgs, fee, account_number, sequence)

            gas_info = self.estimating_gas(tx)
            gas_limit = int(float(gas_info.gas_used) * DefGasAdjustment)

        fee_amount = Coin(amount=str(int(gas_limit * gas_price_amount)), denom=gas_fee_denom)
        fee = Fee(amount=[fee_amount], gas_limit=gas_limit)
        return tx_builder.sign(msgs, fee, account_number, sequence)

    def estimating_gas(self, tx: Tx) -> GasInfo:
        response = TxClient(self.channel).Simulate(SimulateRequest(tx=tx))
        return response.gas_info

    def broadcast_tx(self, tx: Tx, mode: BroadcastMode = BROADCAST_MODE_SYNC) -> TxResponse:
        tx_raw = TxRaw(body_bytes=tx.body.SerializeToString(),
                       auth_info_bytes=tx.auth_info.SerializeToString(),
                       signatures=tx.signatures)
        tx_bytes = tx_raw.SerializeToString()
        response = TxClient(self.channel).BroadcastTx(
            BroadcastTxRequest(tx_bytes=tx_bytes, mode=mode))
        return response.tx_response

    def build_and_broadcast_tx(self, tx_builder: TxBuilder, msgs: [Any], account_number: int = -1, sequence: int = -1,
                               gas_limit: int = 0, mode: BroadcastMode = BROADCAST_MODE_SYNC) -> TxResponse:
        tx = self.build_tx(tx_builder, msgs, account_number, sequence, gas_limit)
        return self.broadcast_tx(tx, mode)

    def wait_mint_tx(self, tx_hash: str, timeout: int = 5, poll_interval: int = 1) -> TxResponse:
        for i in range(timeout // poll_interval):
            time.sleep(poll_interval)
            try:
                response = self.query_tx(tx_hash)
                return response.tx_response
            except grpc.RpcError:
                continue
        raise Exception("not found tx")
