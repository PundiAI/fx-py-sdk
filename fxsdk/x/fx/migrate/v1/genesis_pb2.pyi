from fxpysdk.fxsdk.x.fx.migrate.v1 import migrate_pb2 as _migrate_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["migrate_records"]
    MIGRATE_RECORDS_FIELD_NUMBER: _ClassVar[int]
    migrate_records: _containers.RepeatedCompositeFieldContainer[_migrate_pb2.MigrateRecord]
    def __init__(self, migrate_records: _Optional[_Iterable[_Union[_migrate_pb2.MigrateRecord, _Mapping]]] = ...) -> None: ...
