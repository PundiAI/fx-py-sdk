from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ConfigResponse(_message.Message):
    __slots__ = ["minimum_gas_price"]
    MINIMUM_GAS_PRICE_FIELD_NUMBER: _ClassVar[int]
    minimum_gas_price: str
    def __init__(self, minimum_gas_price: _Optional[str] = ...) -> None: ...
