from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["constant_fee"]
    CONSTANT_FEE_FIELD_NUMBER: _ClassVar[int]
    constant_fee: _coin_pb2.Coin
    def __init__(self, constant_fee: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ...) -> None: ...
