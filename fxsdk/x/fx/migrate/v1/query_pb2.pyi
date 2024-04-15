from fxpysdk.fxsdk.x.fx.migrate.v1 import migrate_pb2 as _migrate_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryMigrateRecordRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class QueryMigrateRecordResponse(_message.Message):
    __slots__ = ["found", "migrateRecord"]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MIGRATERECORD_FIELD_NUMBER: _ClassVar[int]
    found: bool
    migrateRecord: _migrate_pb2.MigrateRecord
    def __init__(self, found: bool = ..., migrateRecord: _Optional[_Union[_migrate_pb2.MigrateRecord, _Mapping]] = ...) -> None: ...

class QueryMigrateCheckAccountRequest(_message.Message):
    __slots__ = ["to"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    to: str
    def __init__(self, to: _Optional[str] = ..., **kwargs) -> None: ...

class QueryMigrateCheckAccountResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
