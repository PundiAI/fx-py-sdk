from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StorageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    STORAGE_TYPE_DEFAULT_UNSPECIFIED: _ClassVar[StorageType]
    STORAGE_TYPE_MEMORY: _ClassVar[StorageType]
    STORAGE_TYPE_TRANSIENT: _ClassVar[StorageType]
    STORAGE_TYPE_INDEX: _ClassVar[StorageType]
    STORAGE_TYPE_COMMITMENT: _ClassVar[StorageType]
STORAGE_TYPE_DEFAULT_UNSPECIFIED: StorageType
STORAGE_TYPE_MEMORY: StorageType
STORAGE_TYPE_TRANSIENT: StorageType
STORAGE_TYPE_INDEX: StorageType
STORAGE_TYPE_COMMITMENT: StorageType
MODULE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
module_schema: _descriptor.FieldDescriptor

class ModuleSchemaDescriptor(_message.Message):
    __slots__ = ["schema_file", "prefix"]
    class FileEntry(_message.Message):
        __slots__ = ["id", "proto_file_name", "storage_type"]
        ID_FIELD_NUMBER: _ClassVar[int]
        PROTO_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        STORAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        id: int
        proto_file_name: str
        storage_type: StorageType
        def __init__(self, id: _Optional[int] = ..., proto_file_name: _Optional[str] = ..., storage_type: _Optional[_Union[StorageType, str]] = ...) -> None: ...
    SCHEMA_FILE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    schema_file: _containers.RepeatedCompositeFieldContainer[ModuleSchemaDescriptor.FileEntry]
    prefix: bytes
    def __init__(self, schema_file: _Optional[_Iterable[_Union[ModuleSchemaDescriptor.FileEntry, _Mapping]]] = ..., prefix: _Optional[bytes] = ...) -> None: ...
