from fxpysdk.fxsdk.x.ethermint.feemarket.v1 import feemarket_pb2 as _feemarket_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["params", "block_gas"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_GAS_FIELD_NUMBER: _ClassVar[int]
    params: _feemarket_pb2.Params
    block_gas: int
    def __init__(self, params: _Optional[_Union[_feemarket_pb2.Params, _Mapping]] = ..., block_gas: _Optional[int] = ...) -> None: ...
