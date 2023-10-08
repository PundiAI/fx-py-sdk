from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.mint.v1beta1 import mint_pb2 as _mint_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["minter", "params"]
    MINTER_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    minter: _mint_pb2.Minter
    params: _mint_pb2.Params
    def __init__(self, minter: _Optional[_Union[_mint_pb2.Minter, _Mapping]] = ..., params: _Optional[_Union[_mint_pb2.Params, _Mapping]] = ...) -> None: ...
