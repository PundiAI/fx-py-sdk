from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExtensionOptionDynamicFeeTx(_message.Message):
    __slots__ = ["max_priority_price"]
    MAX_PRIORITY_PRICE_FIELD_NUMBER: _ClassVar[int]
    max_priority_price: str
    def __init__(self, max_priority_price: _Optional[str] = ...) -> None: ...
