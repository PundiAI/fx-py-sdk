from google.api import annotations_pb2 as _annotations_pb2
from fxsdk.x.fx.dex.v1 import order_pb2 as _order_pb2
from fxsdk.x.fx.dex.v1 import match_pb2 as _match_pb2
from fxsdk.x.fx.dex.v1 import position_pb2 as _position_pb2
from fxsdk.x.fx.dex.v1 import params_pb2 as _params_pb2
from fxsdk.x.fx.dex.v1 import funding_pb2 as _funding_pb2
from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryReserveReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryReserveResp(_message.Message):
    __slots__ = ["reserve"]
    RESERVE_FIELD_NUMBER: _ClassVar[int]
    reserve: _params_pb2.Reserve
    def __init__(self, reserve: _Optional[_Union[_params_pb2.Reserve, _Mapping]] = ...) -> None: ...

class QueryIsFundingReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryIsFundingResp(_message.Message):
    __slots__ = ["is_funding"]
    IS_FUNDING_FIELD_NUMBER: _ClassVar[int]
    is_funding: bool
    def __init__(self, is_funding: bool = ...) -> None: ...

class QueryStoreStatisticReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryStoreStatisticResp(_message.Message):
    __slots__ = ["store_order_num", "orderbook_size", "orderbook_length"]
    STORE_ORDER_NUM_FIELD_NUMBER: _ClassVar[int]
    ORDERBOOK_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORDERBOOK_LENGTH_FIELD_NUMBER: _ClassVar[int]
    store_order_num: int
    orderbook_size: int
    orderbook_length: int
    def __init__(self, store_order_num: _Optional[int] = ..., orderbook_size: _Optional[int] = ..., orderbook_length: _Optional[int] = ...) -> None: ...

class QueryMAReq(_message.Message):
    __slots__ = ["pair_id"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    def __init__(self, pair_id: _Optional[str] = ...) -> None: ...

class QueryMAResp(_message.Message):
    __slots__ = ["average_price", "price2"]
    AVERAGE_PRICE_FIELD_NUMBER: _ClassVar[int]
    PRICE2_FIELD_NUMBER: _ClassVar[int]
    average_price: _containers.RepeatedScalarFieldContainer[str]
    price2: str
    def __init__(self, average_price: _Optional[_Iterable[str]] = ..., price2: _Optional[str] = ...) -> None: ...

class QueryMarkAndOraclePriceReq(_message.Message):
    __slots__ = ["pair_id", "query_all"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_ALL_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    query_all: bool
    def __init__(self, pair_id: _Optional[str] = ..., query_all: bool = ...) -> None: ...

class QueryMarkAndOraclePriceResp(_message.Message):
    __slots__ = ["prices"]
    PRICES_FIELD_NUMBER: _ClassVar[int]
    prices: _containers.RepeatedCompositeFieldContainer[MarkAndOraclePrice]
    def __init__(self, prices: _Optional[_Iterable[_Union[MarkAndOraclePrice, _Mapping]]] = ...) -> None: ...

class QueryParamsReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryParamsResp(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _params_pb2.Params
    def __init__(self, params: _Optional[_Union[_params_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryOrdersRequest(_message.Message):
    __slots__ = ["owner", "pair_id", "page", "limit"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    owner: str
    pair_id: str
    page: str
    limit: str
    def __init__(self, owner: _Optional[str] = ..., pair_id: _Optional[str] = ..., page: _Optional[str] = ..., limit: _Optional[str] = ...) -> None: ...

class QueryOrdersResponse(_message.Message):
    __slots__ = ["orders"]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[_order_pb2.Order]
    def __init__(self, orders: _Optional[_Iterable[_Union[_order_pb2.Order, _Mapping]]] = ...) -> None: ...

class QueryOrderRequest(_message.Message):
    __slots__ = ["order_id"]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    def __init__(self, order_id: _Optional[str] = ...) -> None: ...

class QueryOrderResponse(_message.Message):
    __slots__ = ["order"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: _order_pb2.Order
    def __init__(self, order: _Optional[_Union[_order_pb2.Order, _Mapping]] = ...) -> None: ...

class QueryOrderbookReq(_message.Message):
    __slots__ = ["pair_id"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    def __init__(self, pair_id: _Optional[str] = ...) -> None: ...

class QueryOrderbookResp(_message.Message):
    __slots__ = ["Asks", "Bids"]
    ASKS_FIELD_NUMBER: _ClassVar[int]
    BIDS_FIELD_NUMBER: _ClassVar[int]
    Asks: _containers.RepeatedCompositeFieldContainer[_match_pb2.OrderDepth]
    Bids: _containers.RepeatedCompositeFieldContainer[_match_pb2.OrderDepth]
    def __init__(self, Asks: _Optional[_Iterable[_Union[_match_pb2.OrderDepth, _Mapping]]] = ..., Bids: _Optional[_Iterable[_Union[_match_pb2.OrderDepth, _Mapping]]] = ...) -> None: ...

class QueryPositionsReq(_message.Message):
    __slots__ = ["owner", "direction", "pair_id", "page", "limit"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    owner: str
    direction: _position_pb2.PosDirection
    pair_id: str
    page: str
    limit: str
    def __init__(self, owner: _Optional[str] = ..., direction: _Optional[_Union[_position_pb2.PosDirection, str]] = ..., pair_id: _Optional[str] = ..., page: _Optional[str] = ..., limit: _Optional[str] = ...) -> None: ...

class QueryPositionsResp(_message.Message):
    __slots__ = ["positions"]
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    positions: _containers.RepeatedCompositeFieldContainer[_position_pb2.Position]
    def __init__(self, positions: _Optional[_Iterable[_Union[_position_pb2.Position, _Mapping]]] = ...) -> None: ...

class QueryPositionReq(_message.Message):
    __slots__ = ["owner", "pair_id"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    owner: str
    pair_id: str
    def __init__(self, owner: _Optional[str] = ..., pair_id: _Optional[str] = ...) -> None: ...

class QueryPositionResp(_message.Message):
    __slots__ = ["positions"]
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    positions: _containers.RepeatedCompositeFieldContainer[_position_pb2.Position]
    def __init__(self, positions: _Optional[_Iterable[_Union[_position_pb2.Position, _Mapping]]] = ...) -> None: ...

class QueryFundingReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryFundingResp(_message.Message):
    __slots__ = ["funding"]
    FUNDING_FIELD_NUMBER: _ClassVar[int]
    funding: _funding_pb2.Funding
    def __init__(self, funding: _Optional[_Union[_funding_pb2.Funding, _Mapping]] = ...) -> None: ...

class QueryPairFundingRatesReq(_message.Message):
    __slots__ = ["last_or_realtime"]
    LAST_OR_REALTIME_FIELD_NUMBER: _ClassVar[int]
    last_or_realtime: bool
    def __init__(self, last_or_realtime: bool = ...) -> None: ...

class QueryPairFundingRatesResp(_message.Message):
    __slots__ = ["pair_funding_rates"]
    PAIR_FUNDING_RATES_FIELD_NUMBER: _ClassVar[int]
    pair_funding_rates: _containers.RepeatedCompositeFieldContainer[_funding_pb2.PairFundingRate]
    def __init__(self, pair_funding_rates: _Optional[_Iterable[_Union[_funding_pb2.PairFundingRate, _Mapping]]] = ...) -> None: ...

class QueryFundingTimeReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryFundingTimeResp(_message.Message):
    __slots__ = ["funding_time"]
    FUNDING_TIME_FIELD_NUMBER: _ClassVar[int]
    funding_time: _funding_pb2.FundingTime
    def __init__(self, funding_time: _Optional[_Union[_funding_pb2.FundingTime, _Mapping]] = ...) -> None: ...

class PairPrice(_message.Message):
    __slots__ = ["pair_id", "price"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    price: str
    def __init__(self, pair_id: _Optional[str] = ..., price: _Optional[str] = ...) -> None: ...

class QueryDealPriceReq(_message.Message):
    __slots__ = ["pair_id", "query_all"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_ALL_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    query_all: bool
    def __init__(self, pair_id: _Optional[str] = ..., query_all: bool = ...) -> None: ...

class QueryDealPriceResp(_message.Message):
    __slots__ = ["pair_price"]
    PAIR_PRICE_FIELD_NUMBER: _ClassVar[int]
    pair_price: _containers.RepeatedCompositeFieldContainer[PairPrice]
    def __init__(self, pair_price: _Optional[_Iterable[_Union[PairPrice, _Mapping]]] = ...) -> None: ...

class QueryMatchResultReq(_message.Message):
    __slots__ = ["pair_id", "block_number"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    block_number: int
    def __init__(self, pair_id: _Optional[str] = ..., block_number: _Optional[int] = ...) -> None: ...

class QueryMatchResultResp(_message.Message):
    __slots__ = ["match_result"]
    MATCH_RESULT_FIELD_NUMBER: _ClassVar[int]
    match_result: _match_pb2.MatchResult
    def __init__(self, match_result: _Optional[_Union[_match_pb2.MatchResult, _Mapping]] = ...) -> None: ...

class QueryMarkPriceReq(_message.Message):
    __slots__ = ["pair_id", "query_all"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_ALL_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    query_all: bool
    def __init__(self, pair_id: _Optional[str] = ..., query_all: bool = ...) -> None: ...

class QueryMarkPriceResp(_message.Message):
    __slots__ = ["pair_mark_price"]
    PAIR_MARK_PRICE_FIELD_NUMBER: _ClassVar[int]
    pair_mark_price: _containers.RepeatedCompositeFieldContainer[PairPrice]
    def __init__(self, pair_mark_price: _Optional[_Iterable[_Union[PairPrice, _Mapping]]] = ...) -> None: ...

class MarkAndOraclePrice(_message.Message):
    __slots__ = ["pair_id", "mark_price", "oracle_price"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    MARK_PRICE_FIELD_NUMBER: _ClassVar[int]
    ORACLE_PRICE_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    mark_price: str
    oracle_price: str
    def __init__(self, pair_id: _Optional[str] = ..., mark_price: _Optional[str] = ..., oracle_price: _Optional[str] = ...) -> None: ...

class QueryLiquidationPriceReq(_message.Message):
    __slots__ = ["pair_id", "leverage", "direction", "entry_price", "quantity", "wallet_balance"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ENTRY_PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    WALLET_BALANCE_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    leverage: int
    direction: _position_pb2.PosDirection
    entry_price: str
    quantity: str
    wallet_balance: str
    def __init__(self, pair_id: _Optional[str] = ..., leverage: _Optional[int] = ..., direction: _Optional[_Union[_position_pb2.PosDirection, str]] = ..., entry_price: _Optional[str] = ..., quantity: _Optional[str] = ..., wallet_balance: _Optional[str] = ...) -> None: ...

class QueryLiquidationPriceResp(_message.Message):
    __slots__ = ["liquidation_price"]
    LIQUIDATION_PRICE_FIELD_NUMBER: _ClassVar[int]
    liquidation_price: str
    def __init__(self, liquidation_price: _Optional[str] = ...) -> None: ...

class QueryPremiumIndexConfReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryPremiumIndexConfResp(_message.Message):
    __slots__ = ["premium_index_conf"]
    PREMIUM_INDEX_CONF_FIELD_NUMBER: _ClassVar[int]
    premium_index_conf: _funding_pb2.PremiumIndexConf
    def __init__(self, premium_index_conf: _Optional[_Union[_funding_pb2.PremiumIndexConf, _Mapping]] = ...) -> None: ...

class QueryNeedToLiquidationPosIdsReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryNeedToLiquidatorPosIdsResp(_message.Message):
    __slots__ = ["position_ids", "height"]
    POSITION_IDS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    position_ids: _containers.RepeatedScalarFieldContainer[str]
    height: int
    def __init__(self, position_ids: _Optional[_Iterable[str]] = ..., height: _Optional[int] = ...) -> None: ...

class QueryAccountNumberReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryAccountNumberResp(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...
