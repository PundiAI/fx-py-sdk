from fxpysdk.fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GasPriceRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GasPriceResponse(_message.Message):
    __slots__ = ["gas_prices"]
    GAS_PRICES_FIELD_NUMBER: _ClassVar[int]
    gas_prices: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, gas_prices: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...
