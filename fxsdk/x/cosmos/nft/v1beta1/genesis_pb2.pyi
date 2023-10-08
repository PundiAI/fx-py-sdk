from cosmos.nft.v1beta1 import nft_pb2 as _nft_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["classes", "entries"]
    CLASSES_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    classes: _containers.RepeatedCompositeFieldContainer[_nft_pb2.Class]
    entries: _containers.RepeatedCompositeFieldContainer[Entry]
    def __init__(self, classes: _Optional[_Iterable[_Union[_nft_pb2.Class, _Mapping]]] = ..., entries: _Optional[_Iterable[_Union[Entry, _Mapping]]] = ...) -> None: ...

class Entry(_message.Message):
    __slots__ = ["owner", "nfts"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    NFTS_FIELD_NUMBER: _ClassVar[int]
    owner: str
    nfts: _containers.RepeatedCompositeFieldContainer[_nft_pb2.NFT]
    def __init__(self, owner: _Optional[str] = ..., nfts: _Optional[_Iterable[_Union[_nft_pb2.NFT, _Mapping]]] = ...) -> None: ...
