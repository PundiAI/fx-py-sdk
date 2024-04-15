from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PosDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    POSITIONBOTH: _ClassVar[PosDirection]
    LONG: _ClassVar[PosDirection]
    SHORT: _ClassVar[PosDirection]
POSITIONBOTH: PosDirection
LONG: PosDirection
SHORT: PosDirection

class StoreDec(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class TotalPositionSize(_message.Message):
    __slots__ = ["size"]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    size: str
    def __init__(self, size: _Optional[str] = ...) -> None: ...

class PositionID(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class PositionIDs(_message.Message):
    __slots__ = ["position_ids"]
    POSITION_IDS_FIELD_NUMBER: _ClassVar[int]
    position_ids: _containers.RepeatedCompositeFieldContainer[PositionID]
    def __init__(self, position_ids: _Optional[_Iterable[_Union[PositionID, _Mapping]]] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ["id", "owner", "pair_id", "direction", "entry_price", "mark_price", "liquidation_price", "base_quantity", "margin", "leverage", "unrealized_pnl", "margin_rate", "initial_margin", "pending_order_quantity"]
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ENTRY_PRICE_FIELD_NUMBER: _ClassVar[int]
    MARK_PRICE_FIELD_NUMBER: _ClassVar[int]
    LIQUIDATION_PRICE_FIELD_NUMBER: _ClassVar[int]
    BASE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    MARGIN_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_FIELD_NUMBER: _ClassVar[int]
    UNREALIZED_PNL_FIELD_NUMBER: _ClassVar[int]
    MARGIN_RATE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_MARGIN_FIELD_NUMBER: _ClassVar[int]
    PENDING_ORDER_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    owner: bytes
    pair_id: str
    direction: PosDirection
    entry_price: str
    mark_price: str
    liquidation_price: str
    base_quantity: str
    margin: str
    leverage: int
    unrealized_pnl: str
    margin_rate: str
    initial_margin: str
    pending_order_quantity: str
    def __init__(self, id: _Optional[str] = ..., owner: _Optional[bytes] = ..., pair_id: _Optional[str] = ..., direction: _Optional[_Union[PosDirection, str]] = ..., entry_price: _Optional[str] = ..., mark_price: _Optional[str] = ..., liquidation_price: _Optional[str] = ..., base_quantity: _Optional[str] = ..., margin: _Optional[str] = ..., leverage: _Optional[int] = ..., unrealized_pnl: _Optional[str] = ..., margin_rate: _Optional[str] = ..., initial_margin: _Optional[str] = ..., pending_order_quantity: _Optional[str] = ...) -> None: ...

class Positions(_message.Message):
    __slots__ = ["positions"]
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    positions: _containers.RepeatedCompositeFieldContainer[Position]
    def __init__(self, positions: _Optional[_Iterable[_Union[Position, _Mapping]]] = ...) -> None: ...
