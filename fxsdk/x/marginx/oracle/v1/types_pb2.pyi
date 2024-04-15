from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MarketStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MARKET_STATUS_UNSPECIFIED: _ClassVar[MarketStatus]
    MARKET_STATUS_LISTED: _ClassVar[MarketStatus]
    MARKET_STATUS_SUSPEND: _ClassVar[MarketStatus]
    MARKET_STATUS_PRESET: _ClassVar[MarketStatus]
MARKET_STATUS_UNSPECIFIED: MarketStatus
MARKET_STATUS_LISTED: MarketStatus
MARKET_STATUS_SUSPEND: MarketStatus
MARKET_STATUS_PRESET: MarketStatus

class Params(_message.Message):
    __slots__ = ["price_quote_symbol"]
    PRICE_QUOTE_SYMBOL_FIELD_NUMBER: _ClassVar[int]
    price_quote_symbol: str
    def __init__(self, price_quote_symbol: _Optional[str] = ...) -> None: ...

class Market(_message.Message):
    __slots__ = ["pair_id", "base_asset", "quote_asset", "market_status", "price_decimal", "position_decimal", "type"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_ASSET_FIELD_NUMBER: _ClassVar[int]
    QUOTE_ASSET_FIELD_NUMBER: _ClassVar[int]
    MARKET_STATUS_FIELD_NUMBER: _ClassVar[int]
    PRICE_DECIMAL_FIELD_NUMBER: _ClassVar[int]
    POSITION_DECIMAL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    base_asset: str
    quote_asset: str
    market_status: MarketStatus
    price_decimal: int
    position_decimal: int
    type: str
    def __init__(self, pair_id: _Optional[str] = ..., base_asset: _Optional[str] = ..., quote_asset: _Optional[str] = ..., market_status: _Optional[_Union[MarketStatus, str]] = ..., price_decimal: _Optional[int] = ..., position_decimal: _Optional[int] = ..., type: _Optional[str] = ...) -> None: ...

class Answer(_message.Message):
    __slots__ = ["oracle", "answer"]
    ORACLE_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    oracle: str
    answer: str
    def __init__(self, oracle: _Optional[str] = ..., answer: _Optional[str] = ...) -> None: ...

class Price(_message.Message):
    __slots__ = ["symbol", "value"]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    value: str
    def __init__(self, symbol: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Aggregator(_message.Message):
    __slots__ = ["symbol", "config", "round_start_time", "submissions", "type"]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ROUND_START_TIME_FIELD_NUMBER: _ClassVar[int]
    SUBMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    config: OracleConfig
    round_start_time: int
    submissions: _containers.RepeatedCompositeFieldContainer[Answer]
    type: str
    def __init__(self, symbol: _Optional[str] = ..., config: _Optional[_Union[OracleConfig, _Mapping]] = ..., round_start_time: _Optional[int] = ..., submissions: _Optional[_Iterable[_Union[Answer, _Mapping]]] = ..., type: _Optional[str] = ...) -> None: ...

class OracleConfig(_message.Message):
    __slots__ = ["oracles", "min_answer_threshold", "staleness_threshold"]
    ORACLES_FIELD_NUMBER: _ClassVar[int]
    MIN_ANSWER_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    STALENESS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    oracles: _containers.RepeatedScalarFieldContainer[str]
    min_answer_threshold: int
    staleness_threshold: int
    def __init__(self, oracles: _Optional[_Iterable[str]] = ..., min_answer_threshold: _Optional[int] = ..., staleness_threshold: _Optional[int] = ...) -> None: ...
