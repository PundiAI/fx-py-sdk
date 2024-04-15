from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.fx.dex.v1 import order_pb2 as _order_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrderFill(_message.Message):
    __slots__ = ["order", "deal_price", "quantity_filled", "quantity_unfilled"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    DEAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FILLED_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_UNFILLED_FIELD_NUMBER: _ClassVar[int]
    order: _order_pb2.Order
    deal_price: str
    quantity_filled: str
    quantity_unfilled: str
    def __init__(self, order: _Optional[_Union[_order_pb2.Order, _Mapping]] = ..., deal_price: _Optional[str] = ..., quantity_filled: _Optional[str] = ..., quantity_unfilled: _Optional[str] = ...) -> None: ...

class OrderFills(_message.Message):
    __slots__ = ["order_fill"]
    ORDER_FILL_FIELD_NUMBER: _ClassVar[int]
    order_fill: _containers.RepeatedCompositeFieldContainer[OrderFill]
    def __init__(self, order_fill: _Optional[_Iterable[_Union[OrderFill, _Mapping]]] = ...) -> None: ...

class Price(_message.Message):
    __slots__ = ["price"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    price: str
    def __init__(self, price: _Optional[str] = ...) -> None: ...

class OrderDepth(_message.Message):
    __slots__ = ["price", "quantity"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    price: str
    quantity: str
    def __init__(self, price: _Optional[str] = ..., quantity: _Optional[str] = ...) -> None: ...

class OrderBook(_message.Message):
    __slots__ = ["bid", "ask"]
    BID_FIELD_NUMBER: _ClassVar[int]
    ASK_FIELD_NUMBER: _ClassVar[int]
    bid: _order_pb2.Orders
    ask: _order_pb2.Orders
    def __init__(self, bid: _Optional[_Union[_order_pb2.Orders, _Mapping]] = ..., ask: _Optional[_Union[_order_pb2.Orders, _Mapping]] = ...) -> None: ...

class DepthBookItem(_message.Message):
    __slots__ = ["price", "buy_quantity", "sell_quantity"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    BUY_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SELL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    price: str
    buy_quantity: str
    sell_quantity: str
    def __init__(self, price: _Optional[str] = ..., buy_quantity: _Optional[str] = ..., sell_quantity: _Optional[str] = ...) -> None: ...

class DepthBook(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DepthBookItem]
    def __init__(self, items: _Optional[_Iterable[_Union[DepthBookItem, _Mapping]]] = ...) -> None: ...

class Matcher(_message.Message):
    __slots__ = ["pair_id", "order_book", "last_deal_price", "depth_curves"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_BOOK_FIELD_NUMBER: _ClassVar[int]
    LAST_DEAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    DEPTH_CURVES_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    order_book: OrderBook
    last_deal_price: str
    depth_curves: DepthCurves
    def __init__(self, pair_id: _Optional[str] = ..., order_book: _Optional[_Union[OrderBook, _Mapping]] = ..., last_deal_price: _Optional[str] = ..., depth_curves: _Optional[_Union[DepthCurves, _Mapping]] = ...) -> None: ...

class MatchResult(_message.Message):
    __slots__ = ["pair_id", "bid_count", "ask_count", "deal_price", "matched_bid_volume", "matched_ask_volume", "max_bid_volume", "max_ask_volume", "order_fills"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    BID_COUNT_FIELD_NUMBER: _ClassVar[int]
    ASK_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    MATCHED_BID_VOLUME_FIELD_NUMBER: _ClassVar[int]
    MATCHED_ASK_VOLUME_FIELD_NUMBER: _ClassVar[int]
    MAX_BID_VOLUME_FIELD_NUMBER: _ClassVar[int]
    MAX_ASK_VOLUME_FIELD_NUMBER: _ClassVar[int]
    ORDER_FILLS_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    bid_count: int
    ask_count: int
    deal_price: str
    matched_bid_volume: str
    matched_ask_volume: str
    max_bid_volume: str
    max_ask_volume: str
    order_fills: OrderFills
    def __init__(self, pair_id: _Optional[str] = ..., bid_count: _Optional[int] = ..., ask_count: _Optional[int] = ..., deal_price: _Optional[str] = ..., matched_bid_volume: _Optional[str] = ..., matched_ask_volume: _Optional[str] = ..., max_bid_volume: _Optional[str] = ..., max_ask_volume: _Optional[str] = ..., order_fills: _Optional[_Union[OrderFills, _Mapping]] = ...) -> None: ...

class MatchResults(_message.Message):
    __slots__ = ["match_result"]
    MATCH_RESULT_FIELD_NUMBER: _ClassVar[int]
    match_result: _containers.RepeatedCompositeFieldContainer[MatchResult]
    def __init__(self, match_result: _Optional[_Iterable[_Union[MatchResult, _Mapping]]] = ...) -> None: ...

class DealPrice(_message.Message):
    __slots__ = ["pair_id", "deal_price"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    DEAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    deal_price: str
    def __init__(self, pair_id: _Optional[str] = ..., deal_price: _Optional[str] = ...) -> None: ...

class DepthCurveItem(_message.Message):
    __slots__ = ["price", "sell_quantity", "buy_quantity"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    SELL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    BUY_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    price: str
    sell_quantity: str
    buy_quantity: str
    def __init__(self, price: _Optional[str] = ..., sell_quantity: _Optional[str] = ..., buy_quantity: _Optional[str] = ...) -> None: ...

class DepthCurves(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DepthCurveItem]
    def __init__(self, items: _Optional[_Iterable[_Union[DepthCurveItem, _Mapping]]] = ...) -> None: ...
