from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxpysdk.fxsdk.x.ethermint.evm.v1 import evm_pb2 as _evm_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgEthereumTx(_message.Message):
    __slots__ = ["data", "size", "hash"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    data: _any_pb2.Any
    size: float
    hash: str
    def __init__(self, data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., size: _Optional[float] = ..., hash: _Optional[str] = ..., **kwargs) -> None: ...

class LegacyTx(_message.Message):
    __slots__ = ["nonce", "gas_price", "gas", "to", "value", "data", "v", "r", "s"]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    GAS_PRICE_FIELD_NUMBER: _ClassVar[int]
    GAS_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    S_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    gas_price: str
    gas: int
    to: str
    value: str
    data: bytes
    v: bytes
    r: bytes
    s: bytes
    def __init__(self, nonce: _Optional[int] = ..., gas_price: _Optional[str] = ..., gas: _Optional[int] = ..., to: _Optional[str] = ..., value: _Optional[str] = ..., data: _Optional[bytes] = ..., v: _Optional[bytes] = ..., r: _Optional[bytes] = ..., s: _Optional[bytes] = ...) -> None: ...

class AccessListTx(_message.Message):
    __slots__ = ["chain_id", "nonce", "gas_price", "gas", "to", "value", "data", "accesses", "v", "r", "s"]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    GAS_PRICE_FIELD_NUMBER: _ClassVar[int]
    GAS_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ACCESSES_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    S_FIELD_NUMBER: _ClassVar[int]
    chain_id: str
    nonce: int
    gas_price: str
    gas: int
    to: str
    value: str
    data: bytes
    accesses: _containers.RepeatedCompositeFieldContainer[_evm_pb2.AccessTuple]
    v: bytes
    r: bytes
    s: bytes
    def __init__(self, chain_id: _Optional[str] = ..., nonce: _Optional[int] = ..., gas_price: _Optional[str] = ..., gas: _Optional[int] = ..., to: _Optional[str] = ..., value: _Optional[str] = ..., data: _Optional[bytes] = ..., accesses: _Optional[_Iterable[_Union[_evm_pb2.AccessTuple, _Mapping]]] = ..., v: _Optional[bytes] = ..., r: _Optional[bytes] = ..., s: _Optional[bytes] = ...) -> None: ...

class DynamicFeeTx(_message.Message):
    __slots__ = ["chain_id", "nonce", "gas_tip_cap", "gas_fee_cap", "gas", "to", "value", "data", "accesses", "v", "r", "s"]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    GAS_TIP_CAP_FIELD_NUMBER: _ClassVar[int]
    GAS_FEE_CAP_FIELD_NUMBER: _ClassVar[int]
    GAS_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ACCESSES_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    S_FIELD_NUMBER: _ClassVar[int]
    chain_id: str
    nonce: int
    gas_tip_cap: str
    gas_fee_cap: str
    gas: int
    to: str
    value: str
    data: bytes
    accesses: _containers.RepeatedCompositeFieldContainer[_evm_pb2.AccessTuple]
    v: bytes
    r: bytes
    s: bytes
    def __init__(self, chain_id: _Optional[str] = ..., nonce: _Optional[int] = ..., gas_tip_cap: _Optional[str] = ..., gas_fee_cap: _Optional[str] = ..., gas: _Optional[int] = ..., to: _Optional[str] = ..., value: _Optional[str] = ..., data: _Optional[bytes] = ..., accesses: _Optional[_Iterable[_Union[_evm_pb2.AccessTuple, _Mapping]]] = ..., v: _Optional[bytes] = ..., r: _Optional[bytes] = ..., s: _Optional[bytes] = ...) -> None: ...

class ExtensionOptionsEthereumTx(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgEthereumTxResponse(_message.Message):
    __slots__ = ["hash", "logs", "ret", "vm_error", "gas_used"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    RET_FIELD_NUMBER: _ClassVar[int]
    VM_ERROR_FIELD_NUMBER: _ClassVar[int]
    GAS_USED_FIELD_NUMBER: _ClassVar[int]
    hash: str
    logs: _containers.RepeatedCompositeFieldContainer[_evm_pb2.Log]
    ret: bytes
    vm_error: str
    gas_used: int
    def __init__(self, hash: _Optional[str] = ..., logs: _Optional[_Iterable[_Union[_evm_pb2.Log, _Mapping]]] = ..., ret: _Optional[bytes] = ..., vm_error: _Optional[str] = ..., gas_used: _Optional[int] = ...) -> None: ...
