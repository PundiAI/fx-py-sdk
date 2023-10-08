from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MsgMigrateAccount(_message.Message):
    __slots__ = ["to", "signature"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    to: str
    signature: str
    def __init__(self, to: _Optional[str] = ..., signature: _Optional[str] = ..., **kwargs) -> None: ...

class MsgMigrateAccountResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
