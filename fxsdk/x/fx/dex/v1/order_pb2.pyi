from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BOTH: _ClassVar[Direction]
    BUY: _ClassVar[Direction]
    SELL: _ClassVar[Direction]
    MarketBuy: _ClassVar[Direction]
    MarketSell: _ClassVar[Direction]

class OrderStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ORDER_PENDING: _ClassVar[OrderStatus]
    ORDER_FILLED: _ClassVar[OrderStatus]
    ORDER_PARTIAL_FILLED: _ClassVar[OrderStatus]
    ORDER_CANCELLED: _ClassVar[OrderStatus]
    ORDER_PARTIAL_FILLED_CANCELLED: _ClassVar[OrderStatus]
    ORDER_PARTIAL_FILLED_EXPIRED: _ClassVar[OrderStatus]
    ORDER_EXPIRED: _ClassVar[OrderStatus]
    ORDER_GASOUT: _ClassVar[OrderStatus]
    ORDER_PRICE_LIMIT: _ClassVar[OrderStatus]

class OrderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ORDER_TYPE_OPEN_POSITION: _ClassVar[OrderType]
    ORDER_TYPE_CLOSE_POSITION: _ClassVar[OrderType]
    ORDER_TYPE_LIQUIDATION: _ClassVar[OrderType]
BOTH: Direction
BUY: Direction
SELL: Direction
MarketBuy: Direction
MarketSell: Direction
ORDER_PENDING: OrderStatus
ORDER_FILLED: OrderStatus
ORDER_PARTIAL_FILLED: OrderStatus
ORDER_CANCELLED: OrderStatus
ORDER_PARTIAL_FILLED_CANCELLED: OrderStatus
ORDER_PARTIAL_FILLED_EXPIRED: OrderStatus
ORDER_EXPIRED: OrderStatus
ORDER_GASOUT: OrderStatus
ORDER_PRICE_LIMIT: OrderStatus
ORDER_TYPE_OPEN_POSITION: OrderType
ORDER_TYPE_CLOSE_POSITION: OrderType
ORDER_TYPE_LIQUIDATION: OrderType

class OrderIDs(_message.Message):
    __slots__ = ["ids"]
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ["id", "owner", "pair_id", "direction", "price", "base_quantity", "quote_quantity", "filled_quantity", "filled_avg_price", "leverage", "status", "order_type", "cost_fee", "locked_fee"]
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    BASE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    QUOTE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    FILLED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    FILLED_AVG_PRICE_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    COST_FEE_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FEE_FIELD_NUMBER: _ClassVar[int]
    id: str
    owner: bytes
    pair_id: str
    direction: Direction
    price: str
    base_quantity: str
    quote_quantity: str
    filled_quantity: str
    filled_avg_price: str
    leverage: int
    status: OrderStatus
    order_type: OrderType
    cost_fee: str
    locked_fee: str
    def __init__(self, id: _Optional[str] = ..., owner: _Optional[bytes] = ..., pair_id: _Optional[str] = ..., direction: _Optional[_Union[Direction, str]] = ..., price: _Optional[str] = ..., base_quantity: _Optional[str] = ..., quote_quantity: _Optional[str] = ..., filled_quantity: _Optional[str] = ..., filled_avg_price: _Optional[str] = ..., leverage: _Optional[int] = ..., status: _Optional[_Union[OrderStatus, str]] = ..., order_type: _Optional[_Union[OrderType, str]] = ..., cost_fee: _Optional[str] = ..., locked_fee: _Optional[str] = ...) -> None: ...

class Orders(_message.Message):
    __slots__ = ["orders"]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[Order]
    def __init__(self, orders: _Optional[_Iterable[_Union[Order, _Mapping]]] = ...) -> None: ...
