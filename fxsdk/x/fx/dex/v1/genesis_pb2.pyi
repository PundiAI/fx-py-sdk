from fx.dex.v1 import funding_pb2 as _funding_pb2
from fx.dex.v1 import margin_pb2 as _margin_pb2
from fx.dex.v1 import match_pb2 as _match_pb2
from fx.dex.v1 import order_pb2 as _order_pb2
from fx.dex.v1 import params_pb2 as _params_pb2
from fx.dex.v1 import position_pb2 as _position_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["pair_funding_rates", "funding_info", "funding_time", "premium_index_config", "premium_index", "margin_rate_tables", "deal_price", "orders", "params", "positions", "position_id", "ma_params", "book_pair_ids", "ask_book", "bid_book", "order_book_ids_keys", "order_book_ids", "reserve"]
    PAIR_FUNDING_RATES_FIELD_NUMBER: _ClassVar[int]
    FUNDING_INFO_FIELD_NUMBER: _ClassVar[int]
    FUNDING_TIME_FIELD_NUMBER: _ClassVar[int]
    PREMIUM_INDEX_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PREMIUM_INDEX_FIELD_NUMBER: _ClassVar[int]
    MARGIN_RATE_TABLES_FIELD_NUMBER: _ClassVar[int]
    DEAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    POSITION_ID_FIELD_NUMBER: _ClassVar[int]
    MA_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BOOK_PAIR_IDS_FIELD_NUMBER: _ClassVar[int]
    ASK_BOOK_FIELD_NUMBER: _ClassVar[int]
    BID_BOOK_FIELD_NUMBER: _ClassVar[int]
    ORDER_BOOK_IDS_KEYS_FIELD_NUMBER: _ClassVar[int]
    ORDER_BOOK_IDS_FIELD_NUMBER: _ClassVar[int]
    RESERVE_FIELD_NUMBER: _ClassVar[int]
    pair_funding_rates: _containers.RepeatedCompositeFieldContainer[_funding_pb2.PairFundingRate]
    funding_info: _funding_pb2.Funding
    funding_time: _funding_pb2.FundingTime
    premium_index_config: _funding_pb2.PremiumIndexConf
    premium_index: _containers.RepeatedCompositeFieldContainer[_funding_pb2.PremiumIndex]
    margin_rate_tables: _containers.RepeatedCompositeFieldContainer[_margin_pb2.MarginRateTable]
    deal_price: _containers.RepeatedCompositeFieldContainer[_match_pb2.DealPrice]
    orders: _containers.RepeatedCompositeFieldContainer[_order_pb2.Order]
    params: _params_pb2.Params
    positions: _containers.RepeatedCompositeFieldContainer[_position_pb2.Position]
    position_id: _position_pb2.PositionID
    ma_params: _funding_pb2.MovingAverageParams
    book_pair_ids: _containers.RepeatedScalarFieldContainer[str]
    ask_book: _containers.RepeatedCompositeFieldContainer[OrderDepthArray]
    bid_book: _containers.RepeatedCompositeFieldContainer[OrderDepthArray]
    order_book_ids_keys: _containers.RepeatedScalarFieldContainer[str]
    order_book_ids: _containers.RepeatedCompositeFieldContainer[_order_pb2.OrderIDs]
    reserve: _params_pb2.Reserve
    def __init__(self, pair_funding_rates: _Optional[_Iterable[_Union[_funding_pb2.PairFundingRate, _Mapping]]] = ..., funding_info: _Optional[_Union[_funding_pb2.Funding, _Mapping]] = ..., funding_time: _Optional[_Union[_funding_pb2.FundingTime, _Mapping]] = ..., premium_index_config: _Optional[_Union[_funding_pb2.PremiumIndexConf, _Mapping]] = ..., premium_index: _Optional[_Iterable[_Union[_funding_pb2.PremiumIndex, _Mapping]]] = ..., margin_rate_tables: _Optional[_Iterable[_Union[_margin_pb2.MarginRateTable, _Mapping]]] = ..., deal_price: _Optional[_Iterable[_Union[_match_pb2.DealPrice, _Mapping]]] = ..., orders: _Optional[_Iterable[_Union[_order_pb2.Order, _Mapping]]] = ..., params: _Optional[_Union[_params_pb2.Params, _Mapping]] = ..., positions: _Optional[_Iterable[_Union[_position_pb2.Position, _Mapping]]] = ..., position_id: _Optional[_Union[_position_pb2.PositionID, _Mapping]] = ..., ma_params: _Optional[_Union[_funding_pb2.MovingAverageParams, _Mapping]] = ..., book_pair_ids: _Optional[_Iterable[str]] = ..., ask_book: _Optional[_Iterable[_Union[OrderDepthArray, _Mapping]]] = ..., bid_book: _Optional[_Iterable[_Union[OrderDepthArray, _Mapping]]] = ..., order_book_ids_keys: _Optional[_Iterable[str]] = ..., order_book_ids: _Optional[_Iterable[_Union[_order_pb2.OrderIDs, _Mapping]]] = ..., reserve: _Optional[_Union[_params_pb2.Reserve, _Mapping]] = ...) -> None: ...

class OrderDepthArray(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[_match_pb2.OrderDepth]
    def __init__(self, values: _Optional[_Iterable[_Union[_match_pb2.OrderDepth, _Mapping]]] = ...) -> None: ...
