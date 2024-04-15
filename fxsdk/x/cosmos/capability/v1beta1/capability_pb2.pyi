from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Capability(_message.Message):
    __slots__ = ["index"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    index: int
    def __init__(self, index: _Optional[int] = ...) -> None: ...

class Owner(_message.Message):
    __slots__ = ["module", "name"]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    module: str
    name: str
    def __init__(self, module: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CapabilityOwners(_message.Message):
    __slots__ = ["owners"]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    owners: _containers.RepeatedCompositeFieldContainer[Owner]
    def __init__(self, owners: _Optional[_Iterable[_Union[Owner, _Mapping]]] = ...) -> None: ...
