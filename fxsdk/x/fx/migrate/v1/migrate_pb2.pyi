from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MigrateRecord(_message.Message):
    __slots__ = ["to", "height"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    to: str
    height: int
    def __init__(self, to: _Optional[str] = ..., height: _Optional[int] = ..., **kwargs) -> None: ...
