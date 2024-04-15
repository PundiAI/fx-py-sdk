from fxpysdk.fxsdk.x.cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryEvidenceRequest(_message.Message):
    __slots__ = ["evidence_hash"]
    EVIDENCE_HASH_FIELD_NUMBER: _ClassVar[int]
    evidence_hash: bytes
    def __init__(self, evidence_hash: _Optional[bytes] = ...) -> None: ...

class QueryEvidenceResponse(_message.Message):
    __slots__ = ["evidence"]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    evidence: _any_pb2.Any
    def __init__(self, evidence: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class QueryAllEvidenceRequest(_message.Message):
    __slots__ = ["pagination"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryAllEvidenceResponse(_message.Message):
    __slots__ = ["evidence", "pagination"]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    evidence: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, evidence: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...
