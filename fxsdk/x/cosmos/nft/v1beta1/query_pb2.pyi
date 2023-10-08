from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from google.api import annotations_pb2 as _annotations_pb2
from cosmos.nft.v1beta1 import nft_pb2 as _nft_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryBalanceRequest(_message.Message):
    __slots__ = ["class_id", "owner"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    owner: str
    def __init__(self, class_id: _Optional[str] = ..., owner: _Optional[str] = ...) -> None: ...

class QueryBalanceResponse(_message.Message):
    __slots__ = ["amount"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    amount: int
    def __init__(self, amount: _Optional[int] = ...) -> None: ...

class QueryOwnerRequest(_message.Message):
    __slots__ = ["class_id", "id"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    id: str
    def __init__(self, class_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class QueryOwnerResponse(_message.Message):
    __slots__ = ["owner"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    owner: str
    def __init__(self, owner: _Optional[str] = ...) -> None: ...

class QuerySupplyRequest(_message.Message):
    __slots__ = ["class_id"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    def __init__(self, class_id: _Optional[str] = ...) -> None: ...

class QuerySupplyResponse(_message.Message):
    __slots__ = ["amount"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    amount: int
    def __init__(self, amount: _Optional[int] = ...) -> None: ...

class QueryNFTsRequest(_message.Message):
    __slots__ = ["class_id", "owner", "pagination"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    owner: str
    pagination: _pagination_pb2.PageRequest
    def __init__(self, class_id: _Optional[str] = ..., owner: _Optional[str] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryNFTsResponse(_message.Message):
    __slots__ = ["nfts", "pagination"]
    NFTS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    nfts: _containers.RepeatedCompositeFieldContainer[_nft_pb2.NFT]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, nfts: _Optional[_Iterable[_Union[_nft_pb2.NFT, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryNFTRequest(_message.Message):
    __slots__ = ["class_id", "id"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    id: str
    def __init__(self, class_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class QueryNFTResponse(_message.Message):
    __slots__ = ["nft"]
    NFT_FIELD_NUMBER: _ClassVar[int]
    nft: _nft_pb2.NFT
    def __init__(self, nft: _Optional[_Union[_nft_pb2.NFT, _Mapping]] = ...) -> None: ...

class QueryClassRequest(_message.Message):
    __slots__ = ["class_id"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    def __init__(self, class_id: _Optional[str] = ...) -> None: ...

class QueryClassResponse(_message.Message):
    __slots__ = []
    CLASS_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, **kwargs) -> None: ...

class QueryClassesRequest(_message.Message):
    __slots__ = ["pagination"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PageRequest
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryClassesResponse(_message.Message):
    __slots__ = ["classes", "pagination"]
    CLASSES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    classes: _containers.RepeatedCompositeFieldContainer[_nft_pb2.Class]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, classes: _Optional[_Iterable[_Union[_nft_pb2.Class, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...
