from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from cosmos.upgrade.v1beta1 import upgrade_pb2 as _upgrade_pb2
from cosmos.msg.v1 import msg_pb2 as _msg_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgSoftwareUpgrade(_message.Message):
    __slots__ = ["authority", "plan"]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    authority: str
    plan: _upgrade_pb2.Plan
    def __init__(self, authority: _Optional[str] = ..., plan: _Optional[_Union[_upgrade_pb2.Plan, _Mapping]] = ...) -> None: ...

class MsgSoftwareUpgradeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgCancelUpgrade(_message.Message):
    __slots__ = ["authority"]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    authority: str
    def __init__(self, authority: _Optional[str] = ...) -> None: ...

class MsgCancelUpgradeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
