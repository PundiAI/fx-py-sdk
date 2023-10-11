from google.api import annotations_pb2 as _annotations_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from marginx.oracle.v1 import types_pb2 as _types_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryMarketRequest(_message.Message):
    __slots__ = ["pair_id"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    def __init__(self, pair_id: _Optional[str] = ...) -> None: ...

class QueryMarketResponse(_message.Message):
    __slots__ = ["market"]
    MARKET_FIELD_NUMBER: _ClassVar[int]
    market: _types_pb2.Market
    def __init__(self, market: _Optional[_Union[_types_pb2.Market, _Mapping]] = ...) -> None: ...

class QueryMarketsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryMarketsResponse(_message.Message):
    __slots__ = ["markets"]
    MARKETS_FIELD_NUMBER: _ClassVar[int]
    markets: _containers.RepeatedCompositeFieldContainer[_types_pb2.Market]
    def __init__(self, markets: _Optional[_Iterable[_Union[_types_pb2.Market, _Mapping]]] = ...) -> None: ...

class QueryPriceRequest(_message.Message):
    __slots__ = ["pair_id"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    def __init__(self, pair_id: _Optional[str] = ...) -> None: ...

class QueryPriceResponse(_message.Message):
    __slots__ = ["price"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    price: str
    def __init__(self, price: _Optional[str] = ...) -> None: ...

class QueryPricesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PairPrice(_message.Message):
    __slots__ = ["pair_id", "price"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    price: str
    def __init__(self, pair_id: _Optional[str] = ..., price: _Optional[str] = ...) -> None: ...

class QueryPricesResponse(_message.Message):
    __slots__ = ["prices"]
    PRICES_FIELD_NUMBER: _ClassVar[int]
    prices: _containers.RepeatedCompositeFieldContainer[PairPrice]
    def __init__(self, prices: _Optional[_Iterable[_Union[PairPrice, _Mapping]]] = ...) -> None: ...

class QueryParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _types_pb2.Params
    def __init__(self, params: _Optional[_Union[_types_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryAggregatorsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryAggregatorsResponse(_message.Message):
    __slots__ = ["aggregators"]
    AGGREGATORS_FIELD_NUMBER: _ClassVar[int]
    aggregators: _containers.RepeatedCompositeFieldContainer[_types_pb2.Aggregator]
    def __init__(self, aggregators: _Optional[_Iterable[_Union[_types_pb2.Aggregator, _Mapping]]] = ...) -> None: ...
