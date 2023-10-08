from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MultiSignature(_message.Message):
    __slots__ = ["signatures"]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    signatures: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, signatures: _Optional[_Iterable[bytes]] = ...) -> None: ...

class CompactBitArray(_message.Message):
    __slots__ = ["extra_bits_stored", "elems"]
    EXTRA_BITS_STORED_FIELD_NUMBER: _ClassVar[int]
    ELEMS_FIELD_NUMBER: _ClassVar[int]
    extra_bits_stored: int
    elems: bytes
    def __init__(self, extra_bits_stored: _Optional[int] = ..., elems: _Optional[bytes] = ...) -> None: ...
