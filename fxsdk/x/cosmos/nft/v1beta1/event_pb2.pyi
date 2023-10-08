from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EventSend(_message.Message):
    __slots__ = ["class_id", "id", "sender", "receiver"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    id: str
    sender: str
    receiver: str
    def __init__(self, class_id: _Optional[str] = ..., id: _Optional[str] = ..., sender: _Optional[str] = ..., receiver: _Optional[str] = ...) -> None: ...

class EventMint(_message.Message):
    __slots__ = ["class_id", "id", "owner"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    id: str
    owner: str
    def __init__(self, class_id: _Optional[str] = ..., id: _Optional[str] = ..., owner: _Optional[str] = ...) -> None: ...

class EventBurn(_message.Message):
    __slots__ = ["class_id", "id", "owner"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    id: str
    owner: str
    def __init__(self, class_id: _Optional[str] = ..., id: _Optional[str] = ..., owner: _Optional[str] = ...) -> None: ...
