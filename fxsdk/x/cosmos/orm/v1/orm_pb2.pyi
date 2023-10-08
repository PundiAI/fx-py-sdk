from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
TABLE_FIELD_NUMBER: _ClassVar[int]
table: _descriptor.FieldDescriptor
SINGLETON_FIELD_NUMBER: _ClassVar[int]
singleton: _descriptor.FieldDescriptor

class TableDescriptor(_message.Message):
    __slots__ = ["primary_key", "index", "id"]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    primary_key: PrimaryKeyDescriptor
    index: _containers.RepeatedCompositeFieldContainer[SecondaryIndexDescriptor]
    id: int
    def __init__(self, primary_key: _Optional[_Union[PrimaryKeyDescriptor, _Mapping]] = ..., index: _Optional[_Iterable[_Union[SecondaryIndexDescriptor, _Mapping]]] = ..., id: _Optional[int] = ...) -> None: ...

class PrimaryKeyDescriptor(_message.Message):
    __slots__ = ["fields", "auto_increment"]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    AUTO_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    fields: str
    auto_increment: bool
    def __init__(self, fields: _Optional[str] = ..., auto_increment: bool = ...) -> None: ...

class SecondaryIndexDescriptor(_message.Message):
    __slots__ = ["fields", "id", "unique"]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_FIELD_NUMBER: _ClassVar[int]
    fields: str
    id: int
    unique: bool
    def __init__(self, fields: _Optional[str] = ..., id: _Optional[int] = ..., unique: bool = ...) -> None: ...

class SingletonDescriptor(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...
