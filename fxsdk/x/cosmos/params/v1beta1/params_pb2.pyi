from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParameterChangeProposal(_message.Message):
    __slots__ = ["title", "description", "changes"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    changes: _containers.RepeatedCompositeFieldContainer[ParamChange]
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., changes: _Optional[_Iterable[_Union[ParamChange, _Mapping]]] = ...) -> None: ...

class ParamChange(_message.Message):
    __slots__ = ["subspace", "key", "value"]
    SUBSPACE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    subspace: str
    key: str
    value: str
    def __init__(self, subspace: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
