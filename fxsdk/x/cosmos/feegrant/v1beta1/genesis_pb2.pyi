from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.feegrant.v1beta1 import feegrant_pb2 as _feegrant_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["allowances"]
    ALLOWANCES_FIELD_NUMBER: _ClassVar[int]
    allowances: _containers.RepeatedCompositeFieldContainer[_feegrant_pb2.Grant]
    def __init__(self, allowances: _Optional[_Iterable[_Union[_feegrant_pb2.Grant, _Mapping]]] = ...) -> None: ...
