from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PairFundingRate(_message.Message):
    __slots__ = ["pair_id", "funding_rate", "funding_time"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    FUNDING_RATE_FIELD_NUMBER: _ClassVar[int]
    FUNDING_TIME_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    funding_rate: str
    funding_time: int
    def __init__(self, pair_id: _Optional[str] = ..., funding_rate: _Optional[str] = ..., funding_time: _Optional[int] = ...) -> None: ...

class Funding(_message.Message):
    __slots__ = ["funding_period", "next_funding_time", "funding_times", "max_funding_per_block", "crypto_funding_period", "crypto_next_funding_time", "crypto_funding_times"]
    FUNDING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    NEXT_FUNDING_TIME_FIELD_NUMBER: _ClassVar[int]
    FUNDING_TIMES_FIELD_NUMBER: _ClassVar[int]
    MAX_FUNDING_PER_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_FUNDING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_NEXT_FUNDING_TIME_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_FUNDING_TIMES_FIELD_NUMBER: _ClassVar[int]
    funding_period: int
    next_funding_time: int
    funding_times: int
    max_funding_per_block: int
    crypto_funding_period: int
    crypto_next_funding_time: int
    crypto_funding_times: int
    def __init__(self, funding_period: _Optional[int] = ..., next_funding_time: _Optional[int] = ..., funding_times: _Optional[int] = ..., max_funding_per_block: _Optional[int] = ..., crypto_funding_period: _Optional[int] = ..., crypto_next_funding_time: _Optional[int] = ..., crypto_funding_times: _Optional[int] = ...) -> None: ...

class FundingTime(_message.Message):
    __slots__ = ["summer_time", "winter_time", "summer_clocks", "winter_clocks", "holidays", "crypto_clocks"]
    SUMMER_TIME_FIELD_NUMBER: _ClassVar[int]
    WINTER_TIME_FIELD_NUMBER: _ClassVar[int]
    SUMMER_CLOCKS_FIELD_NUMBER: _ClassVar[int]
    WINTER_CLOCKS_FIELD_NUMBER: _ClassVar[int]
    HOLIDAYS_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_CLOCKS_FIELD_NUMBER: _ClassVar[int]
    summer_time: int
    winter_time: int
    summer_clocks: _containers.RepeatedScalarFieldContainer[str]
    winter_clocks: _containers.RepeatedScalarFieldContainer[str]
    holidays: _containers.RepeatedScalarFieldContainer[str]
    crypto_clocks: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, summer_time: _Optional[int] = ..., winter_time: _Optional[int] = ..., summer_clocks: _Optional[_Iterable[str]] = ..., winter_clocks: _Optional[_Iterable[str]] = ..., holidays: _Optional[_Iterable[str]] = ..., crypto_clocks: _Optional[_Iterable[str]] = ...) -> None: ...

class SettleFunding(_message.Message):
    __slots__ = ["is_funding", "next_position_id", "market_type"]
    IS_FUNDING_FIELD_NUMBER: _ClassVar[int]
    NEXT_POSITION_ID_FIELD_NUMBER: _ClassVar[int]
    MARKET_TYPE_FIELD_NUMBER: _ClassVar[int]
    is_funding: bool
    next_position_id: str
    market_type: str
    def __init__(self, is_funding: bool = ..., next_position_id: _Optional[str] = ..., market_type: _Optional[str] = ...) -> None: ...

class PremiumIndexConf(_message.Message):
    __slots__ = ["update_period", "next_update_time", "round_start_time", "next_round_time", "round_index", "crypto_update_period", "crypto_next_update_time", "crypto_round_start_time", "crypto_next_round_time", "crypto_round_index"]
    UPDATE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    NEXT_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ROUND_START_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_ROUND_TIME_FIELD_NUMBER: _ClassVar[int]
    ROUND_INDEX_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_UPDATE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_NEXT_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_ROUND_START_TIME_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_NEXT_ROUND_TIME_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_ROUND_INDEX_FIELD_NUMBER: _ClassVar[int]
    update_period: int
    next_update_time: int
    round_start_time: int
    next_round_time: int
    round_index: int
    crypto_update_period: int
    crypto_next_update_time: int
    crypto_round_start_time: int
    crypto_next_round_time: int
    crypto_round_index: int
    def __init__(self, update_period: _Optional[int] = ..., next_update_time: _Optional[int] = ..., round_start_time: _Optional[int] = ..., next_round_time: _Optional[int] = ..., round_index: _Optional[int] = ..., crypto_update_period: _Optional[int] = ..., crypto_next_update_time: _Optional[int] = ..., crypto_round_start_time: _Optional[int] = ..., crypto_next_round_time: _Optional[int] = ..., crypto_round_index: _Optional[int] = ...) -> None: ...

class PremiumIndex(_message.Message):
    __slots__ = ["pair_id", "round_timestamp", "ticks"]
    class Tick(_message.Message):
        __slots__ = ["value", "ts"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TS_FIELD_NUMBER: _ClassVar[int]
        value: str
        ts: int
        def __init__(self, value: _Optional[str] = ..., ts: _Optional[int] = ...) -> None: ...
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    ROUND_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TICKS_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    round_timestamp: int
    ticks: _containers.RepeatedCompositeFieldContainer[PremiumIndex.Tick]
    def __init__(self, pair_id: _Optional[str] = ..., round_timestamp: _Optional[int] = ..., ticks: _Optional[_Iterable[_Union[PremiumIndex.Tick, _Mapping]]] = ...) -> None: ...

class MovingAverageParams(_message.Message):
    __slots__ = ["update_period", "next_update_time"]
    UPDATE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    NEXT_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    update_period: int
    next_update_time: int
    def __init__(self, update_period: _Optional[int] = ..., next_update_time: _Optional[int] = ...) -> None: ...

class MovingAverage(_message.Message):
    __slots__ = ["average_price"]
    AVERAGE_PRICE_FIELD_NUMBER: _ClassVar[int]
    average_price: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, average_price: _Optional[_Iterable[str]] = ...) -> None: ...
