from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
MODULE_FIELD_NUMBER: _ClassVar[int]
module: _descriptor.FieldDescriptor

class ModuleDescriptor(_message.Message):
    __slots__ = ["go_import", "use_package", "can_migrate_from"]
    GO_IMPORT_FIELD_NUMBER: _ClassVar[int]
    USE_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    CAN_MIGRATE_FROM_FIELD_NUMBER: _ClassVar[int]
    go_import: str
    use_package: _containers.RepeatedCompositeFieldContainer[PackageReference]
    can_migrate_from: _containers.RepeatedCompositeFieldContainer[MigrateFromInfo]
    def __init__(self, go_import: _Optional[str] = ..., use_package: _Optional[_Iterable[_Union[PackageReference, _Mapping]]] = ..., can_migrate_from: _Optional[_Iterable[_Union[MigrateFromInfo, _Mapping]]] = ...) -> None: ...

class PackageReference(_message.Message):
    __slots__ = ["name", "revision"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision: int
    def __init__(self, name: _Optional[str] = ..., revision: _Optional[int] = ...) -> None: ...

class MigrateFromInfo(_message.Message):
    __slots__ = ["module"]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    module: str
    def __init__(self, module: _Optional[str] = ...) -> None: ...
