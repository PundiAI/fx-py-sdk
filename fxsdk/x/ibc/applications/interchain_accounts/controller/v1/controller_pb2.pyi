from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ["controller_enabled"]
    CONTROLLER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    controller_enabled: bool
    def __init__(self, controller_enabled: bool = ...) -> None: ...
