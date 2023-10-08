from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Snapshot(_message.Message):
    __slots__ = ["height", "format", "chunks", "hash", "metadata"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    height: int
    format: int
    chunks: int
    hash: bytes
    metadata: Metadata
    def __init__(self, height: _Optional[int] = ..., format: _Optional[int] = ..., chunks: _Optional[int] = ..., hash: _Optional[bytes] = ..., metadata: _Optional[_Union[Metadata, _Mapping]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ["chunk_hashes"]
    CHUNK_HASHES_FIELD_NUMBER: _ClassVar[int]
    chunk_hashes: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, chunk_hashes: _Optional[_Iterable[bytes]] = ...) -> None: ...

class SnapshotItem(_message.Message):
    __slots__ = ["store", "iavl", "extension", "extension_payload", "kv", "schema"]
    STORE_FIELD_NUMBER: _ClassVar[int]
    IAVL_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    KV_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    store: SnapshotStoreItem
    iavl: SnapshotIAVLItem
    extension: SnapshotExtensionMeta
    extension_payload: SnapshotExtensionPayload
    kv: SnapshotKVItem
    schema: SnapshotSchema
    def __init__(self, store: _Optional[_Union[SnapshotStoreItem, _Mapping]] = ..., iavl: _Optional[_Union[SnapshotIAVLItem, _Mapping]] = ..., extension: _Optional[_Union[SnapshotExtensionMeta, _Mapping]] = ..., extension_payload: _Optional[_Union[SnapshotExtensionPayload, _Mapping]] = ..., kv: _Optional[_Union[SnapshotKVItem, _Mapping]] = ..., schema: _Optional[_Union[SnapshotSchema, _Mapping]] = ...) -> None: ...

class SnapshotStoreItem(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SnapshotIAVLItem(_message.Message):
    __slots__ = ["key", "value", "version", "height"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    value: bytes
    version: int
    height: int
    def __init__(self, key: _Optional[bytes] = ..., value: _Optional[bytes] = ..., version: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class SnapshotExtensionMeta(_message.Message):
    __slots__ = ["name", "format"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    name: str
    format: int
    def __init__(self, name: _Optional[str] = ..., format: _Optional[int] = ...) -> None: ...

class SnapshotExtensionPayload(_message.Message):
    __slots__ = ["payload"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    def __init__(self, payload: _Optional[bytes] = ...) -> None: ...

class SnapshotKVItem(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    value: bytes
    def __init__(self, key: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...

class SnapshotSchema(_message.Message):
    __slots__ = ["keys"]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, keys: _Optional[_Iterable[bytes]] = ...) -> None: ...
