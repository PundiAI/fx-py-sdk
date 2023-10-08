from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Class(_message.Message):
    __slots__ = ["id", "name", "symbol", "description", "uri", "uri_hash", "data"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    URI_HASH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    symbol: str
    description: str
    uri: str
    uri_hash: str
    data: _any_pb2.Any
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., symbol: _Optional[str] = ..., description: _Optional[str] = ..., uri: _Optional[str] = ..., uri_hash: _Optional[str] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class NFT(_message.Message):
    __slots__ = ["class_id", "id", "uri", "uri_hash", "data"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    URI_HASH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    id: str
    uri: str
    uri_hash: str
    data: _any_pb2.Any
    def __init__(self, class_id: _Optional[str] = ..., id: _Optional[str] = ..., uri: _Optional[str] = ..., uri_hash: _Optional[str] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
