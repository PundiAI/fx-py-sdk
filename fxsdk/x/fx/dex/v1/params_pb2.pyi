from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ["fee_rate", "force_liquidation_margin_rate_threshold", "max_deals_per_block", "max_orders_per_account", "permitted_max_leverage", "lock_coin_factor", "fx_discount", "discount_denom", "min_funding_rate", "max_funding_rate"]
    FEE_RATE_FIELD_NUMBER: _ClassVar[int]
    FORCE_LIQUIDATION_MARGIN_RATE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_DEALS_PER_BLOCK_FIELD_NUMBER: _ClassVar[int]
    MAX_ORDERS_PER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PERMITTED_MAX_LEVERAGE_FIELD_NUMBER: _ClassVar[int]
    LOCK_COIN_FACTOR_FIELD_NUMBER: _ClassVar[int]
    FX_DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_DENOM_FIELD_NUMBER: _ClassVar[int]
    MIN_FUNDING_RATE_FIELD_NUMBER: _ClassVar[int]
    MAX_FUNDING_RATE_FIELD_NUMBER: _ClassVar[int]
    fee_rate: str
    force_liquidation_margin_rate_threshold: int
    max_deals_per_block: int
    max_orders_per_account: int
    permitted_max_leverage: int
    lock_coin_factor: str
    fx_discount: str
    discount_denom: str
    min_funding_rate: str
    max_funding_rate: str
    def __init__(self, fee_rate: _Optional[str] = ..., force_liquidation_margin_rate_threshold: _Optional[int] = ..., max_deals_per_block: _Optional[int] = ..., max_orders_per_account: _Optional[int] = ..., permitted_max_leverage: _Optional[int] = ..., lock_coin_factor: _Optional[str] = ..., fx_discount: _Optional[str] = ..., discount_denom: _Optional[str] = ..., min_funding_rate: _Optional[str] = ..., max_funding_rate: _Optional[str] = ...) -> None: ...

class Reserve(_message.Message):
    __slots__ = ["accumulative_fee", "risk_reserve", "locked_funds", "short_pay_margin", "long_pay_margin"]
    ACCUMULATIVE_FEE_FIELD_NUMBER: _ClassVar[int]
    RISK_RESERVE_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FUNDS_FIELD_NUMBER: _ClassVar[int]
    SHORT_PAY_MARGIN_FIELD_NUMBER: _ClassVar[int]
    LONG_PAY_MARGIN_FIELD_NUMBER: _ClassVar[int]
    accumulative_fee: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    risk_reserve: str
    locked_funds: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    short_pay_margin: str
    long_pay_margin: str
    def __init__(self, accumulative_fee: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., risk_reserve: _Optional[str] = ..., locked_funds: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., short_pay_margin: _Optional[str] = ..., long_pay_margin: _Optional[str] = ...) -> None: ...
