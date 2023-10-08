from google.protobuf import any_pb2 as _any_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Plan(_message.Message):
    __slots__ = ["name", "time", "height", "info", "upgraded_client_state"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    UPGRADED_CLIENT_STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    time: _timestamp_pb2.Timestamp
    height: int
    info: str
    upgraded_client_state: _any_pb2.Any
    def __init__(self, name: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., height: _Optional[int] = ..., info: _Optional[str] = ..., upgraded_client_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class SoftwareUpgradeProposal(_message.Message):
    __slots__ = ["title", "description", "plan"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    plan: Plan
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., plan: _Optional[_Union[Plan, _Mapping]] = ...) -> None: ...

class CancelSoftwareUpgradeProposal(_message.Message):
    __slots__ = ["title", "description"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class ModuleVersion(_message.Message):
    __slots__ = ["name", "version"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: int
    def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...
