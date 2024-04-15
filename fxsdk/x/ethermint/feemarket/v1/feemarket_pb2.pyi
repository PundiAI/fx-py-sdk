from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ["no_base_fee", "base_fee_change_denominator", "elasticity_multiplier", "enable_height", "base_fee", "min_gas_price", "min_gas_multiplier"]
    NO_BASE_FEE_FIELD_NUMBER: _ClassVar[int]
    BASE_FEE_CHANGE_DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    ELASTICITY_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BASE_FEE_FIELD_NUMBER: _ClassVar[int]
    MIN_GAS_PRICE_FIELD_NUMBER: _ClassVar[int]
    MIN_GAS_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    no_base_fee: bool
    base_fee_change_denominator: int
    elasticity_multiplier: int
    enable_height: int
    base_fee: str
    min_gas_price: str
    min_gas_multiplier: str
    def __init__(self, no_base_fee: bool = ..., base_fee_change_denominator: _Optional[int] = ..., elasticity_multiplier: _Optional[int] = ..., enable_height: _Optional[int] = ..., base_fee: _Optional[str] = ..., min_gas_price: _Optional[str] = ..., min_gas_multiplier: _Optional[str] = ...) -> None: ...
