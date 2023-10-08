from gogoproto import gogo_pb2 as _gogo_pb2
from fx.dex.v1 import order_pb2 as _order_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from cosmos.msg.v1 import msg_pb2 as _msg_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgCreateOrder(_message.Message):
    __slots__ = ["owner", "pair_id", "direction", "price", "base_quantity", "leverage"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    BASE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_FIELD_NUMBER: _ClassVar[int]
    owner: str
    pair_id: str
    direction: _order_pb2.Direction
    price: str
    base_quantity: str
    leverage: int
    def __init__(self, owner: _Optional[str] = ..., pair_id: _Optional[str] = ..., direction: _Optional[_Union[_order_pb2.Direction, str]] = ..., price: _Optional[str] = ..., base_quantity: _Optional[str] = ..., leverage: _Optional[int] = ...) -> None: ...

class MsgCreateOrderResponse(_message.Message):
    __slots__ = ["order_id"]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    def __init__(self, order_id: _Optional[str] = ...) -> None: ...

class MsgCancelOrder(_message.Message):
    __slots__ = ["owner", "order_id"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    owner: str
    order_id: str
    def __init__(self, owner: _Optional[str] = ..., order_id: _Optional[str] = ...) -> None: ...

class MsgCancelOrderResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgAddMargin(_message.Message):
    __slots__ = ["owner", "pair_id", "position_id", "margin"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_ID_FIELD_NUMBER: _ClassVar[int]
    MARGIN_FIELD_NUMBER: _ClassVar[int]
    owner: str
    pair_id: str
    position_id: str
    margin: str
    def __init__(self, owner: _Optional[str] = ..., pair_id: _Optional[str] = ..., position_id: _Optional[str] = ..., margin: _Optional[str] = ...) -> None: ...

class MsgAddMarginResp(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgClosePosition(_message.Message):
    __slots__ = ["owner", "pair_id", "position_id", "price", "base_quantity", "full_close", "market_close"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    BASE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    FULL_CLOSE_FIELD_NUMBER: _ClassVar[int]
    MARKET_CLOSE_FIELD_NUMBER: _ClassVar[int]
    owner: str
    pair_id: str
    position_id: str
    price: str
    base_quantity: str
    full_close: bool
    market_close: bool
    def __init__(self, owner: _Optional[str] = ..., pair_id: _Optional[str] = ..., position_id: _Optional[str] = ..., price: _Optional[str] = ..., base_quantity: _Optional[str] = ..., full_close: bool = ..., market_close: bool = ...) -> None: ...

class MsgClosePositionResp(_message.Message):
    __slots__ = ["order_id"]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    def __init__(self, order_id: _Optional[str] = ...) -> None: ...

class MsgLiquidationPosition(_message.Message):
    __slots__ = ["liquidator", "position_ids"]
    LIQUIDATOR_FIELD_NUMBER: _ClassVar[int]
    POSITION_IDS_FIELD_NUMBER: _ClassVar[int]
    liquidator: str
    position_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, liquidator: _Optional[str] = ..., position_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class MsgLiquidationPositionResp(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgFundDexPool(_message.Message):
    __slots__ = ["amount", "depositor"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DEPOSITOR_FIELD_NUMBER: _ClassVar[int]
    amount: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    depositor: str
    def __init__(self, amount: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., depositor: _Optional[str] = ...) -> None: ...

class MsgFundDexPoolResp(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
