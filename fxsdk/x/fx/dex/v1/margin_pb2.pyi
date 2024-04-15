from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MarginRateTable(_message.Message):
    __slots__ = ["pair_id", "leverage", "nominal_position", "maint_margin_rate", "maint_amount", "Leverages", "Rates", "impact_price_base_amount"]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_POSITION_FIELD_NUMBER: _ClassVar[int]
    MAINT_MARGIN_RATE_FIELD_NUMBER: _ClassVar[int]
    MAINT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    LEVERAGES_FIELD_NUMBER: _ClassVar[int]
    RATES_FIELD_NUMBER: _ClassVar[int]
    IMPACT_PRICE_BASE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    pair_id: str
    leverage: int
    nominal_position: _containers.RepeatedScalarFieldContainer[str]
    maint_margin_rate: _containers.RepeatedScalarFieldContainer[str]
    maint_amount: _containers.RepeatedScalarFieldContainer[str]
    Leverages: _containers.RepeatedScalarFieldContainer[int]
    Rates: _containers.RepeatedScalarFieldContainer[str]
    impact_price_base_amount: str
    def __init__(self, pair_id: _Optional[str] = ..., leverage: _Optional[int] = ..., nominal_position: _Optional[_Iterable[str]] = ..., maint_margin_rate: _Optional[_Iterable[str]] = ..., maint_amount: _Optional[_Iterable[str]] = ..., Leverages: _Optional[_Iterable[int]] = ..., Rates: _Optional[_Iterable[str]] = ..., impact_price_base_amount: _Optional[str] = ...) -> None: ...
