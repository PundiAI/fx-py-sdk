from fxsdk.x.fx.legacy.gravity.v1 import genesis_pb2 as _genesis_pb2
from fxsdk.x.fx.legacy.gravity.v1 import tx_pb2 as _tx_pb2
from fxsdk.x.fx.legacy.gravity.v1 import types_pb2 as _types_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _genesis_pb2.Params
    def __init__(self, params: _Optional[_Union[_genesis_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryCurrentValsetRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryCurrentValsetResponse(_message.Message):
    __slots__ = ["valset"]
    VALSET_FIELD_NUMBER: _ClassVar[int]
    valset: _types_pb2.Valset
    def __init__(self, valset: _Optional[_Union[_types_pb2.Valset, _Mapping]] = ...) -> None: ...

class QueryValsetRequestRequest(_message.Message):
    __slots__ = ["nonce"]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    def __init__(self, nonce: _Optional[int] = ...) -> None: ...

class QueryValsetRequestResponse(_message.Message):
    __slots__ = ["valset"]
    VALSET_FIELD_NUMBER: _ClassVar[int]
    valset: _types_pb2.Valset
    def __init__(self, valset: _Optional[_Union[_types_pb2.Valset, _Mapping]] = ...) -> None: ...

class QueryValsetConfirmRequest(_message.Message):
    __slots__ = ["nonce", "address"]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    address: str
    def __init__(self, nonce: _Optional[int] = ..., address: _Optional[str] = ...) -> None: ...

class QueryValsetConfirmResponse(_message.Message):
    __slots__ = ["confirm"]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    confirm: _tx_pb2.MsgValsetConfirm
    def __init__(self, confirm: _Optional[_Union[_tx_pb2.MsgValsetConfirm, _Mapping]] = ...) -> None: ...

class QueryValsetConfirmsByNonceRequest(_message.Message):
    __slots__ = ["nonce"]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    def __init__(self, nonce: _Optional[int] = ...) -> None: ...

class QueryValsetConfirmsByNonceResponse(_message.Message):
    __slots__ = ["confirms"]
    CONFIRMS_FIELD_NUMBER: _ClassVar[int]
    confirms: _containers.RepeatedCompositeFieldContainer[_tx_pb2.MsgValsetConfirm]
    def __init__(self, confirms: _Optional[_Iterable[_Union[_tx_pb2.MsgValsetConfirm, _Mapping]]] = ...) -> None: ...

class QueryLastValsetRequestsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryLastValsetRequestsResponse(_message.Message):
    __slots__ = ["valsets"]
    VALSETS_FIELD_NUMBER: _ClassVar[int]
    valsets: _containers.RepeatedCompositeFieldContainer[_types_pb2.Valset]
    def __init__(self, valsets: _Optional[_Iterable[_Union[_types_pb2.Valset, _Mapping]]] = ...) -> None: ...

class QueryLastPendingValsetRequestByAddrRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class QueryLastPendingValsetRequestByAddrResponse(_message.Message):
    __slots__ = ["valsets"]
    VALSETS_FIELD_NUMBER: _ClassVar[int]
    valsets: _containers.RepeatedCompositeFieldContainer[_types_pb2.Valset]
    def __init__(self, valsets: _Optional[_Iterable[_Union[_types_pb2.Valset, _Mapping]]] = ...) -> None: ...

class QueryBatchFeeRequest(_message.Message):
    __slots__ = ["minBatchFees"]
    MINBATCHFEES_FIELD_NUMBER: _ClassVar[int]
    minBatchFees: _containers.RepeatedCompositeFieldContainer[_types_pb2.MinBatchFee]
    def __init__(self, minBatchFees: _Optional[_Iterable[_Union[_types_pb2.MinBatchFee, _Mapping]]] = ...) -> None: ...

class QueryBatchFeeResponse(_message.Message):
    __slots__ = ["batch_fees"]
    BATCH_FEES_FIELD_NUMBER: _ClassVar[int]
    batch_fees: _containers.RepeatedCompositeFieldContainer[_types_pb2.BatchFees]
    def __init__(self, batch_fees: _Optional[_Iterable[_Union[_types_pb2.BatchFees, _Mapping]]] = ...) -> None: ...

class QueryLastPendingBatchRequestByAddrRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class QueryLastPendingBatchRequestByAddrResponse(_message.Message):
    __slots__ = ["batch"]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    batch: _types_pb2.OutgoingTxBatch
    def __init__(self, batch: _Optional[_Union[_types_pb2.OutgoingTxBatch, _Mapping]] = ...) -> None: ...

class QueryOutgoingTxBatchesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryOutgoingTxBatchesResponse(_message.Message):
    __slots__ = ["batches"]
    BATCHES_FIELD_NUMBER: _ClassVar[int]
    batches: _containers.RepeatedCompositeFieldContainer[_types_pb2.OutgoingTxBatch]
    def __init__(self, batches: _Optional[_Iterable[_Union[_types_pb2.OutgoingTxBatch, _Mapping]]] = ...) -> None: ...

class QueryBatchRequestByNonceRequest(_message.Message):
    __slots__ = ["nonce", "token_contract"]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    token_contract: str
    def __init__(self, nonce: _Optional[int] = ..., token_contract: _Optional[str] = ...) -> None: ...

class QueryBatchRequestByNonceResponse(_message.Message):
    __slots__ = ["batch"]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    batch: _types_pb2.OutgoingTxBatch
    def __init__(self, batch: _Optional[_Union[_types_pb2.OutgoingTxBatch, _Mapping]] = ...) -> None: ...

class QueryBatchConfirmRequest(_message.Message):
    __slots__ = ["nonce", "token_contract", "address"]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    token_contract: str
    address: str
    def __init__(self, nonce: _Optional[int] = ..., token_contract: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...

class QueryBatchConfirmResponse(_message.Message):
    __slots__ = ["confirm"]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    confirm: _tx_pb2.MsgConfirmBatch
    def __init__(self, confirm: _Optional[_Union[_tx_pb2.MsgConfirmBatch, _Mapping]] = ...) -> None: ...

class QueryBatchConfirmsRequest(_message.Message):
    __slots__ = ["nonce", "token_contract"]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    token_contract: str
    def __init__(self, nonce: _Optional[int] = ..., token_contract: _Optional[str] = ...) -> None: ...

class QueryBatchConfirmsResponse(_message.Message):
    __slots__ = ["confirms"]
    CONFIRMS_FIELD_NUMBER: _ClassVar[int]
    confirms: _containers.RepeatedCompositeFieldContainer[_tx_pb2.MsgConfirmBatch]
    def __init__(self, confirms: _Optional[_Iterable[_Union[_tx_pb2.MsgConfirmBatch, _Mapping]]] = ...) -> None: ...

class QueryLastEventNonceByAddrRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class QueryLastEventNonceByAddrResponse(_message.Message):
    __slots__ = ["event_nonce"]
    EVENT_NONCE_FIELD_NUMBER: _ClassVar[int]
    event_nonce: int
    def __init__(self, event_nonce: _Optional[int] = ...) -> None: ...

class QueryERC20ToDenomRequest(_message.Message):
    __slots__ = ["erc20"]
    ERC20_FIELD_NUMBER: _ClassVar[int]
    erc20: str
    def __init__(self, erc20: _Optional[str] = ...) -> None: ...

class QueryERC20ToDenomResponse(_message.Message):
    __slots__ = ["denom", "fx_originated"]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    FX_ORIGINATED_FIELD_NUMBER: _ClassVar[int]
    denom: str
    fx_originated: bool
    def __init__(self, denom: _Optional[str] = ..., fx_originated: bool = ...) -> None: ...

class QueryDenomToERC20Request(_message.Message):
    __slots__ = ["denom"]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    denom: str
    def __init__(self, denom: _Optional[str] = ...) -> None: ...

class QueryDenomToERC20Response(_message.Message):
    __slots__ = ["erc20", "fx_originated"]
    ERC20_FIELD_NUMBER: _ClassVar[int]
    FX_ORIGINATED_FIELD_NUMBER: _ClassVar[int]
    erc20: str
    fx_originated: bool
    def __init__(self, erc20: _Optional[str] = ..., fx_originated: bool = ...) -> None: ...

class QueryDelegateKeyByValidatorRequest(_message.Message):
    __slots__ = ["validator_address"]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    validator_address: str
    def __init__(self, validator_address: _Optional[str] = ...) -> None: ...

class QueryDelegateKeyByValidatorResponse(_message.Message):
    __slots__ = ["eth_address", "orchestrator_address"]
    ETH_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    eth_address: str
    orchestrator_address: str
    def __init__(self, eth_address: _Optional[str] = ..., orchestrator_address: _Optional[str] = ...) -> None: ...

class QueryDelegateKeyByEthRequest(_message.Message):
    __slots__ = ["eth_address"]
    ETH_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    eth_address: str
    def __init__(self, eth_address: _Optional[str] = ...) -> None: ...

class QueryDelegateKeyByEthResponse(_message.Message):
    __slots__ = ["validator_address", "orchestrator_address"]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    validator_address: str
    orchestrator_address: str
    def __init__(self, validator_address: _Optional[str] = ..., orchestrator_address: _Optional[str] = ...) -> None: ...

class QueryDelegateKeyByOrchestratorRequest(_message.Message):
    __slots__ = ["orchestrator_address"]
    ORCHESTRATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    orchestrator_address: str
    def __init__(self, orchestrator_address: _Optional[str] = ...) -> None: ...

class QueryDelegateKeyByOrchestratorResponse(_message.Message):
    __slots__ = ["validator_address", "eth_address"]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ETH_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    validator_address: str
    eth_address: str
    def __init__(self, validator_address: _Optional[str] = ..., eth_address: _Optional[str] = ...) -> None: ...

class QueryPendingSendToEthRequest(_message.Message):
    __slots__ = ["sender_address"]
    SENDER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    sender_address: str
    def __init__(self, sender_address: _Optional[str] = ...) -> None: ...

class QueryPendingSendToEthResponse(_message.Message):
    __slots__ = ["transfers_in_batches", "unbatched_transfers"]
    TRANSFERS_IN_BATCHES_FIELD_NUMBER: _ClassVar[int]
    UNBATCHED_TRANSFERS_FIELD_NUMBER: _ClassVar[int]
    transfers_in_batches: _containers.RepeatedCompositeFieldContainer[_types_pb2.OutgoingTransferTx]
    unbatched_transfers: _containers.RepeatedCompositeFieldContainer[_types_pb2.OutgoingTransferTx]
    def __init__(self, transfers_in_batches: _Optional[_Iterable[_Union[_types_pb2.OutgoingTransferTx, _Mapping]]] = ..., unbatched_transfers: _Optional[_Iterable[_Union[_types_pb2.OutgoingTransferTx, _Mapping]]] = ...) -> None: ...

class QueryLastObservedBlockHeightRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryLastObservedBlockHeightResponse(_message.Message):
    __slots__ = ["eth_block_height", "block_height"]
    ETH_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    eth_block_height: int
    block_height: int
    def __init__(self, eth_block_height: _Optional[int] = ..., block_height: _Optional[int] = ...) -> None: ...

class QueryLastEventBlockHeightByAddrRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class QueryLastEventBlockHeightByAddrResponse(_message.Message):
    __slots__ = ["block_height"]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    block_height: int
    def __init__(self, block_height: _Optional[int] = ...) -> None: ...

class QueryProjectedBatchTimeoutHeightRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryProjectedBatchTimeoutHeightResponse(_message.Message):
    __slots__ = ["timeout_height"]
    TIMEOUT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    timeout_height: int
    def __init__(self, timeout_height: _Optional[int] = ...) -> None: ...

class QueryBridgeTokensRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryBridgeTokensResponse(_message.Message):
    __slots__ = ["bridge_tokens"]
    BRIDGE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    bridge_tokens: _containers.RepeatedCompositeFieldContainer[_types_pb2.ERC20ToDenom]
    def __init__(self, bridge_tokens: _Optional[_Iterable[_Union[_types_pb2.ERC20ToDenom, _Mapping]]] = ...) -> None: ...
