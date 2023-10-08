from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.capability.v1beta1 import capability_pb2 as _capability_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisOwners(_message.Message):
    __slots__ = ["index", "index_owners"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    INDEX_OWNERS_FIELD_NUMBER: _ClassVar[int]
    index: int
    index_owners: _capability_pb2.CapabilityOwners
    def __init__(self, index: _Optional[int] = ..., index_owners: _Optional[_Union[_capability_pb2.CapabilityOwners, _Mapping]] = ...) -> None: ...

class GenesisState(_message.Message):
    __slots__ = ["index", "owners"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    index: int
    owners: _containers.RepeatedCompositeFieldContainer[GenesisOwners]
    def __init__(self, index: _Optional[int] = ..., owners: _Optional[_Iterable[_Union[GenesisOwners, _Mapping]]] = ...) -> None: ...
