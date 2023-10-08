from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommitInfo(_message.Message):
    __slots__ = ["version", "store_infos"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STORE_INFOS_FIELD_NUMBER: _ClassVar[int]
    version: int
    store_infos: _containers.RepeatedCompositeFieldContainer[StoreInfo]
    def __init__(self, version: _Optional[int] = ..., store_infos: _Optional[_Iterable[_Union[StoreInfo, _Mapping]]] = ...) -> None: ...

class StoreInfo(_message.Message):
    __slots__ = ["name", "commit_id"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMIT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    commit_id: CommitID
    def __init__(self, name: _Optional[str] = ..., commit_id: _Optional[_Union[CommitID, _Mapping]] = ...) -> None: ...

class CommitID(_message.Message):
    __slots__ = ["version", "hash"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    version: int
    hash: bytes
    def __init__(self, version: _Optional[int] = ..., hash: _Optional[bytes] = ...) -> None: ...
