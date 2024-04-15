from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
import proofs_pb2 as _proofs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MerkleRoot(_message.Message):
    __slots__ = ["hash"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: bytes
    def __init__(self, hash: _Optional[bytes] = ...) -> None: ...

class MerklePrefix(_message.Message):
    __slots__ = ["key_prefix"]
    KEY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    key_prefix: bytes
    def __init__(self, key_prefix: _Optional[bytes] = ...) -> None: ...

class MerklePath(_message.Message):
    __slots__ = ["key_path"]
    KEY_PATH_FIELD_NUMBER: _ClassVar[int]
    key_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key_path: _Optional[_Iterable[str]] = ...) -> None: ...

class MerkleProof(_message.Message):
    __slots__ = ["proofs"]
    PROOFS_FIELD_NUMBER: _ClassVar[int]
    proofs: _containers.RepeatedCompositeFieldContainer[_proofs_pb2.CommitmentProof]
    def __init__(self, proofs: _Optional[_Iterable[_Union[_proofs_pb2.CommitmentProof, _Mapping]]] = ...) -> None: ...
