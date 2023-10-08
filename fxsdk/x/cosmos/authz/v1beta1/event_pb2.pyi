from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EventGrant(_message.Message):
    __slots__ = ["msg_type_url", "granter", "grantee"]
    MSG_TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    msg_type_url: str
    granter: str
    grantee: str
    def __init__(self, msg_type_url: _Optional[str] = ..., granter: _Optional[str] = ..., grantee: _Optional[str] = ...) -> None: ...

class EventRevoke(_message.Message):
    __slots__ = ["msg_type_url", "granter", "grantee"]
    MSG_TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    GRANTER_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_FIELD_NUMBER: _ClassVar[int]
    msg_type_url: str
    granter: str
    grantee: str
    def __init__(self, msg_type_url: _Optional[str] = ..., granter: _Optional[str] = ..., grantee: _Optional[str] = ...) -> None: ...
