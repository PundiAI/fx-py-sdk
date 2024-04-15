from fxpysdk.fxsdk.x.cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from fxpysdk.fxsdk.x.ethermint.evm.v1 import evm_pb2 as _evm_pb2
from fxpysdk.fxsdk.x.ethermint.evm.v1 import tx_pb2 as _tx_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryAccountRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class QueryAccountResponse(_message.Message):
    __slots__ = ["balance", "code_hash", "nonce"]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    CODE_HASH_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    balance: str
    code_hash: str
    nonce: int
    def __init__(self, balance: _Optional[str] = ..., code_hash: _Optional[str] = ..., nonce: _Optional[int] = ...) -> None: ...

class QueryCosmosAccountRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class QueryCosmosAccountResponse(_message.Message):
    __slots__ = ["cosmos_address", "sequence", "account_number"]
    COSMOS_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    cosmos_address: str
    sequence: int
    account_number: int
    def __init__(self, cosmos_address: _Optional[str] = ..., sequence: _Optional[int] = ..., account_number: _Optional[int] = ...) -> None: ...

class QueryValidatorAccountRequest(_message.Message):
    __slots__ = ["cons_address"]
    CONS_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    cons_address: str
    def __init__(self, cons_address: _Optional[str] = ...) -> None: ...

class QueryValidatorAccountResponse(_message.Message):
    __slots__ = ["account_address", "sequence", "account_number"]
    ACCOUNT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    account_address: str
    sequence: int
    account_number: int
    def __init__(self, account_address: _Optional[str] = ..., sequence: _Optional[int] = ..., account_number: _Optional[int] = ...) -> None: ...

class QueryBalanceRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class QueryBalanceResponse(_message.Message):
    __slots__ = ["balance"]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    balance: str
    def __init__(self, balance: _Optional[str] = ...) -> None: ...

class QueryStorageRequest(_message.Message):
    __slots__ = ["address", "key"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    address: str
    key: str
    def __init__(self, address: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class QueryStorageResponse(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class QueryCodeRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class QueryCodeResponse(_message.Message):
    __slots__ = ["code"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: bytes
    def __init__(self, code: _Optional[bytes] = ...) -> None: ...

class QueryTxLogsRequest(_message.Message):
    __slots__ = ["hash", "pagination"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    hash: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, hash: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryTxLogsResponse(_message.Message):
    __slots__ = ["logs", "pagination"]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    logs: _containers.RepeatedCompositeFieldContainer[_evm_pb2.Log]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, logs: _Optional[_Iterable[_Union[_evm_pb2.Log, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _evm_pb2.Params
    def __init__(self, params: _Optional[_Union[_evm_pb2.Params, _Mapping]] = ...) -> None: ...

class EthCallRequest(_message.Message):
    __slots__ = ["args", "gas_cap", "proposer_address", "chain_id"]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    GAS_CAP_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    args: bytes
    gas_cap: int
    proposer_address: bytes
    chain_id: int
    def __init__(self, args: _Optional[bytes] = ..., gas_cap: _Optional[int] = ..., proposer_address: _Optional[bytes] = ..., chain_id: _Optional[int] = ...) -> None: ...

class EstimateGasResponse(_message.Message):
    __slots__ = ["gas"]
    GAS_FIELD_NUMBER: _ClassVar[int]
    gas: int
    def __init__(self, gas: _Optional[int] = ...) -> None: ...

class QueryTraceTxRequest(_message.Message):
    __slots__ = ["msg", "trace_config", "predecessors", "block_number", "block_hash", "block_time", "proposer_address", "chain_id"]
    MSG_FIELD_NUMBER: _ClassVar[int]
    TRACE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PREDECESSORS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    BLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    msg: _tx_pb2.MsgEthereumTx
    trace_config: _evm_pb2.TraceConfig
    predecessors: _containers.RepeatedCompositeFieldContainer[_tx_pb2.MsgEthereumTx]
    block_number: int
    block_hash: str
    block_time: _timestamp_pb2.Timestamp
    proposer_address: bytes
    chain_id: int
    def __init__(self, msg: _Optional[_Union[_tx_pb2.MsgEthereumTx, _Mapping]] = ..., trace_config: _Optional[_Union[_evm_pb2.TraceConfig, _Mapping]] = ..., predecessors: _Optional[_Iterable[_Union[_tx_pb2.MsgEthereumTx, _Mapping]]] = ..., block_number: _Optional[int] = ..., block_hash: _Optional[str] = ..., block_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., proposer_address: _Optional[bytes] = ..., chain_id: _Optional[int] = ...) -> None: ...

class QueryTraceTxResponse(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class QueryTraceBlockRequest(_message.Message):
    __slots__ = ["txs", "trace_config", "block_number", "block_hash", "block_time", "proposer_address", "chain_id"]
    TXS_FIELD_NUMBER: _ClassVar[int]
    TRACE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BLOCK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    BLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    txs: _containers.RepeatedCompositeFieldContainer[_tx_pb2.MsgEthereumTx]
    trace_config: _evm_pb2.TraceConfig
    block_number: int
    block_hash: str
    block_time: _timestamp_pb2.Timestamp
    proposer_address: bytes
    chain_id: int
    def __init__(self, txs: _Optional[_Iterable[_Union[_tx_pb2.MsgEthereumTx, _Mapping]]] = ..., trace_config: _Optional[_Union[_evm_pb2.TraceConfig, _Mapping]] = ..., block_number: _Optional[int] = ..., block_hash: _Optional[str] = ..., block_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., proposer_address: _Optional[bytes] = ..., chain_id: _Optional[int] = ...) -> None: ...

class QueryTraceBlockResponse(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class QueryBaseFeeRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryBaseFeeResponse(_message.Message):
    __slots__ = ["base_fee"]
    BASE_FEE_FIELD_NUMBER: _ClassVar[int]
    base_fee: str
    def __init__(self, base_fee: _Optional[str] = ...) -> None: ...
