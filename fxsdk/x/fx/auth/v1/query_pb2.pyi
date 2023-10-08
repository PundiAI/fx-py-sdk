from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConvertAddressRequest(_message.Message):
    __slots__ = ["address", "prefix"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    address: str
    prefix: str
    def __init__(self, address: _Optional[str] = ..., prefix: _Optional[str] = ...) -> None: ...

class ConvertAddressResponse(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...
