from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["gen_txs"]
    GEN_TXS_FIELD_NUMBER: _ClassVar[int]
    gen_txs: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, gen_txs: _Optional[_Iterable[bytes]] = ...) -> None: ...
