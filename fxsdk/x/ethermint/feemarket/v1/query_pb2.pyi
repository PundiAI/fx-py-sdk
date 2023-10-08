from gogoproto import gogo_pb2 as _gogo_pb2
from ethermint.feemarket.v1 import feemarket_pb2 as _feemarket_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _feemarket_pb2.Params
    def __init__(self, params: _Optional[_Union[_feemarket_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryBaseFeeRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryBaseFeeResponse(_message.Message):
    __slots__ = ["base_fee"]
    BASE_FEE_FIELD_NUMBER: _ClassVar[int]
    base_fee: str
    def __init__(self, base_fee: _Optional[str] = ...) -> None: ...

class QueryBlockGasRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryBlockGasResponse(_message.Message):
    __slots__ = ["gas"]
    GAS_FIELD_NUMBER: _ClassVar[int]
    gas: int
    def __init__(self, gas: _Optional[int] = ...) -> None: ...
