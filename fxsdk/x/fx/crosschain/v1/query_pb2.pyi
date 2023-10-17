from fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxsdk.x.fx.crosschain.v1 import tx_pb2 as _tx_pb2
from fxsdk.x.fx.crosschain.v1 import types_pb2 as _types_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryParamsRequest(_message.Message):
    __slots__ = ["chain_name"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    def __init__(self, chain_name: _Optional[str] = ...) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _types_pb2.Params
    def __init__(self, params: _Optional[_Union[_types_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryCurrentOracleSetRequest(_message.Message):
    __slots__ = ["chain_name"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    def __init__(self, chain_name: _Optional[str] = ...) -> None: ...

class QueryCurrentOracleSetResponse(_message.Message):
    __slots__ = ["oracle_set"]
    ORACLE_SET_FIELD_NUMBER: _ClassVar[int]
    oracle_set: _types_pb2.OracleSet
    def __init__(self, oracle_set: _Optional[_Union[_types_pb2.OracleSet, _Mapping]] = ...) -> None: ...

class QueryOracleSetRequestRequest(_message.Message):
    __slots__ = ["chain_name", "nonce"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    nonce: int
    def __init__(self, chain_name: _Optional[str] = ..., nonce: _Optional[int] = ...) -> None: ...

class QueryOracleSetRequestResponse(_message.Message):
    __slots__ = ["oracle_set"]
    ORACLE_SET_FIELD_NUMBER: _ClassVar[int]
    oracle_set: _types_pb2.OracleSet
    def __init__(self, oracle_set: _Optional[_Union[_types_pb2.OracleSet, _Mapping]] = ...) -> None: ...

class QueryOracleSetConfirmRequest(_message.Message):
    __slots__ = ["chain_name", "bridger_address", "nonce"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    bridger_address: str
    nonce: int
    def __init__(self, chain_name: _Optional[str] = ..., bridger_address: _Optional[str] = ..., nonce: _Optional[int] = ...) -> None: ...

class QueryOracleSetConfirmResponse(_message.Message):
    __slots__ = ["confirm"]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    confirm: _tx_pb2.MsgOracleSetConfirm
    def __init__(self, confirm: _Optional[_Union[_tx_pb2.MsgOracleSetConfirm, _Mapping]] = ...) -> None: ...

class QueryOracleSetConfirmsByNonceRequest(_message.Message):
    __slots__ = ["chain_name", "nonce"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    nonce: int
    def __init__(self, chain_name: _Optional[str] = ..., nonce: _Optional[int] = ...) -> None: ...

class QueryOracleSetConfirmsByNonceResponse(_message.Message):
    __slots__ = ["confirms"]
    CONFIRMS_FIELD_NUMBER: _ClassVar[int]
    confirms: _containers.RepeatedCompositeFieldContainer[_tx_pb2.MsgOracleSetConfirm]
    def __init__(self, confirms: _Optional[_Iterable[_Union[_tx_pb2.MsgOracleSetConfirm, _Mapping]]] = ...) -> None: ...

class QueryLastOracleSetRequestsRequest(_message.Message):
    __slots__ = ["chain_name"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    def __init__(self, chain_name: _Optional[str] = ...) -> None: ...

class QueryLastOracleSetRequestsResponse(_message.Message):
    __slots__ = ["oracle_sets"]
    ORACLE_SETS_FIELD_NUMBER: _ClassVar[int]
    oracle_sets: _containers.RepeatedCompositeFieldContainer[_types_pb2.OracleSet]
    def __init__(self, oracle_sets: _Optional[_Iterable[_Union[_types_pb2.OracleSet, _Mapping]]] = ...) -> None: ...

class QueryLastPendingOracleSetRequestByAddrRequest(_message.Message):
    __slots__ = ["chain_name", "bridger_address"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    bridger_address: str
    def __init__(self, chain_name: _Optional[str] = ..., bridger_address: _Optional[str] = ...) -> None: ...

class QueryLastPendingOracleSetRequestByAddrResponse(_message.Message):
    __slots__ = ["oracle_sets"]
    ORACLE_SETS_FIELD_NUMBER: _ClassVar[int]
    oracle_sets: _containers.RepeatedCompositeFieldContainer[_types_pb2.OracleSet]
    def __init__(self, oracle_sets: _Optional[_Iterable[_Union[_types_pb2.OracleSet, _Mapping]]] = ...) -> None: ...

class QueryBatchFeeRequest(_message.Message):
    __slots__ = ["chain_name", "minBatchFees"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    MINBATCHFEES_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    minBatchFees: _containers.RepeatedCompositeFieldContainer[_types_pb2.MinBatchFee]
    def __init__(self, chain_name: _Optional[str] = ..., minBatchFees: _Optional[_Iterable[_Union[_types_pb2.MinBatchFee, _Mapping]]] = ...) -> None: ...

class QueryBatchFeeResponse(_message.Message):
    __slots__ = ["batch_fees"]
    BATCH_FEES_FIELD_NUMBER: _ClassVar[int]
    batch_fees: _containers.RepeatedCompositeFieldContainer[_types_pb2.BatchFees]
    def __init__(self, batch_fees: _Optional[_Iterable[_Union[_types_pb2.BatchFees, _Mapping]]] = ...) -> None: ...

class QueryLastPendingBatchRequestByAddrRequest(_message.Message):
    __slots__ = ["chain_name", "bridger_address"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    bridger_address: str
    def __init__(self, chain_name: _Optional[str] = ..., bridger_address: _Optional[str] = ...) -> None: ...

class QueryLastPendingBatchRequestByAddrResponse(_message.Message):
    __slots__ = ["batch"]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    batch: _types_pb2.OutgoingTxBatch
    def __init__(self, batch: _Optional[_Union[_types_pb2.OutgoingTxBatch, _Mapping]] = ...) -> None: ...

class QueryOutgoingTxBatchesRequest(_message.Message):
    __slots__ = ["chain_name"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    def __init__(self, chain_name: _Optional[str] = ...) -> None: ...

class QueryOutgoingTxBatchesResponse(_message.Message):
    __slots__ = ["batches"]
    BATCHES_FIELD_NUMBER: _ClassVar[int]
    batches: _containers.RepeatedCompositeFieldContainer[_types_pb2.OutgoingTxBatch]
    def __init__(self, batches: _Optional[_Iterable[_Union[_types_pb2.OutgoingTxBatch, _Mapping]]] = ...) -> None: ...

class QueryBatchRequestByNonceRequest(_message.Message):
    __slots__ = ["chain_name", "token_contract", "nonce"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    token_contract: str
    nonce: int
    def __init__(self, chain_name: _Optional[str] = ..., token_contract: _Optional[str] = ..., nonce: _Optional[int] = ...) -> None: ...

class QueryBatchRequestByNonceResponse(_message.Message):
    __slots__ = ["batch"]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    batch: _types_pb2.OutgoingTxBatch
    def __init__(self, batch: _Optional[_Union[_types_pb2.OutgoingTxBatch, _Mapping]] = ...) -> None: ...

class QueryBatchConfirmRequest(_message.Message):
    __slots__ = ["chain_name", "token_contract", "bridger_address", "nonce"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    token_contract: str
    bridger_address: str
    nonce: int
    def __init__(self, chain_name: _Optional[str] = ..., token_contract: _Optional[str] = ..., bridger_address: _Optional[str] = ..., nonce: _Optional[int] = ...) -> None: ...

class QueryBatchConfirmResponse(_message.Message):
    __slots__ = ["confirm"]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    confirm: _tx_pb2.MsgConfirmBatch
    def __init__(self, confirm: _Optional[_Union[_tx_pb2.MsgConfirmBatch, _Mapping]] = ...) -> None: ...

class QueryBatchConfirmsRequest(_message.Message):
    __slots__ = ["chain_name", "token_contract", "nonce"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    token_contract: str
    nonce: int
    def __init__(self, chain_name: _Optional[str] = ..., token_contract: _Optional[str] = ..., nonce: _Optional[int] = ...) -> None: ...

class QueryBatchConfirmsResponse(_message.Message):
    __slots__ = ["confirms"]
    CONFIRMS_FIELD_NUMBER: _ClassVar[int]
    confirms: _containers.RepeatedCompositeFieldContainer[_tx_pb2.MsgConfirmBatch]
    def __init__(self, confirms: _Optional[_Iterable[_Union[_tx_pb2.MsgConfirmBatch, _Mapping]]] = ...) -> None: ...

class QueryLastEventNonceByAddrRequest(_message.Message):
    __slots__ = ["chain_name", "bridger_address"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    bridger_address: str
    def __init__(self, chain_name: _Optional[str] = ..., bridger_address: _Optional[str] = ...) -> None: ...

class QueryLastEventNonceByAddrResponse(_message.Message):
    __slots__ = ["event_nonce"]
    EVENT_NONCE_FIELD_NUMBER: _ClassVar[int]
    event_nonce: int
    def __init__(self, event_nonce: _Optional[int] = ...) -> None: ...

class QueryTokenToDenomRequest(_message.Message):
    __slots__ = ["chain_name", "token"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    token: str
    def __init__(self, chain_name: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class QueryTokenToDenomResponse(_message.Message):
    __slots__ = ["denom"]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    denom: str
    def __init__(self, denom: _Optional[str] = ...) -> None: ...

class QueryDenomToTokenRequest(_message.Message):
    __slots__ = ["chain_name", "denom"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    denom: str
    def __init__(self, chain_name: _Optional[str] = ..., denom: _Optional[str] = ...) -> None: ...

class QueryDenomToTokenResponse(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class QueryOracleByAddrRequest(_message.Message):
    __slots__ = ["chain_name", "oracle_address"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    oracle_address: str
    def __init__(self, chain_name: _Optional[str] = ..., oracle_address: _Optional[str] = ...) -> None: ...

class QueryOracleResponse(_message.Message):
    __slots__ = ["oracle"]
    ORACLE_FIELD_NUMBER: _ClassVar[int]
    oracle: _types_pb2.Oracle
    def __init__(self, oracle: _Optional[_Union[_types_pb2.Oracle, _Mapping]] = ...) -> None: ...

class QueryOracleByExternalAddrRequest(_message.Message):
    __slots__ = ["chain_name", "external_address"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    external_address: str
    def __init__(self, chain_name: _Optional[str] = ..., external_address: _Optional[str] = ...) -> None: ...

class QueryOracleByBridgerAddrRequest(_message.Message):
    __slots__ = ["chain_name", "bridger_address"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    bridger_address: str
    def __init__(self, chain_name: _Optional[str] = ..., bridger_address: _Optional[str] = ...) -> None: ...

class QueryPendingSendToExternalRequest(_message.Message):
    __slots__ = ["chain_name", "sender_address"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    SENDER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    sender_address: str
    def __init__(self, chain_name: _Optional[str] = ..., sender_address: _Optional[str] = ...) -> None: ...

class QueryPendingSendToExternalResponse(_message.Message):
    __slots__ = ["transfers_in_batches", "unbatched_transfers"]
    TRANSFERS_IN_BATCHES_FIELD_NUMBER: _ClassVar[int]
    UNBATCHED_TRANSFERS_FIELD_NUMBER: _ClassVar[int]
    transfers_in_batches: _containers.RepeatedCompositeFieldContainer[_types_pb2.OutgoingTransferTx]
    unbatched_transfers: _containers.RepeatedCompositeFieldContainer[_types_pb2.OutgoingTransferTx]
    def __init__(self, transfers_in_batches: _Optional[_Iterable[_Union[_types_pb2.OutgoingTransferTx, _Mapping]]] = ..., unbatched_transfers: _Optional[_Iterable[_Union[_types_pb2.OutgoingTransferTx, _Mapping]]] = ...) -> None: ...

class QueryLastObservedBlockHeightRequest(_message.Message):
    __slots__ = ["chain_name"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    def __init__(self, chain_name: _Optional[str] = ...) -> None: ...

class QueryLastObservedBlockHeightResponse(_message.Message):
    __slots__ = ["external_block_height", "block_height"]
    EXTERNAL_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    external_block_height: int
    block_height: int
    def __init__(self, external_block_height: _Optional[int] = ..., block_height: _Optional[int] = ...) -> None: ...

class QueryLastEventBlockHeightByAddrRequest(_message.Message):
    __slots__ = ["chain_name", "bridger_address"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    BRIDGER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    bridger_address: str
    def __init__(self, chain_name: _Optional[str] = ..., bridger_address: _Optional[str] = ...) -> None: ...

class QueryLastEventBlockHeightByAddrResponse(_message.Message):
    __slots__ = ["block_height"]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    block_height: int
    def __init__(self, block_height: _Optional[int] = ...) -> None: ...

class QueryOraclesRequest(_message.Message):
    __slots__ = ["chain_name"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    def __init__(self, chain_name: _Optional[str] = ...) -> None: ...

class QueryOraclesResponse(_message.Message):
    __slots__ = ["oracles"]
    ORACLES_FIELD_NUMBER: _ClassVar[int]
    oracles: _containers.RepeatedCompositeFieldContainer[_types_pb2.Oracle]
    def __init__(self, oracles: _Optional[_Iterable[_Union[_types_pb2.Oracle, _Mapping]]] = ...) -> None: ...

class QueryProjectedBatchTimeoutHeightRequest(_message.Message):
    __slots__ = ["chain_name"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    def __init__(self, chain_name: _Optional[str] = ...) -> None: ...

class QueryProjectedBatchTimeoutHeightResponse(_message.Message):
    __slots__ = ["timeout_height"]
    TIMEOUT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    timeout_height: int
    def __init__(self, timeout_height: _Optional[int] = ...) -> None: ...

class QueryBridgeTokensRequest(_message.Message):
    __slots__ = ["chain_name"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    def __init__(self, chain_name: _Optional[str] = ...) -> None: ...

class QueryBridgeTokensResponse(_message.Message):
    __slots__ = ["bridge_tokens"]
    BRIDGE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    bridge_tokens: _containers.RepeatedCompositeFieldContainer[_types_pb2.BridgeToken]
    def __init__(self, bridge_tokens: _Optional[_Iterable[_Union[_types_pb2.BridgeToken, _Mapping]]] = ...) -> None: ...

class QueryBridgeCoinByDenomRequest(_message.Message):
    __slots__ = ["chain_name", "denom"]
    CHAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    chain_name: str
    denom: str
    def __init__(self, chain_name: _Optional[str] = ..., denom: _Optional[str] = ...) -> None: ...

class QueryBridgeCoinByDenomResponse(_message.Message):
    __slots__ = ["coin"]
    COIN_FIELD_NUMBER: _ClassVar[int]
    coin: _coin_pb2.Coin
    def __init__(self, coin: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ...) -> None: ...

class QueryBridgeChainListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryBridgeChainListResponse(_message.Message):
    __slots__ = ["chain_names"]
    CHAIN_NAMES_FIELD_NUMBER: _ClassVar[int]
    chain_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, chain_names: _Optional[_Iterable[str]] = ...) -> None: ...
