from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IncentivizedAcknowledgement(_message.Message):
    __slots__ = ["app_acknowledgement", "forward_relayer_address", "underlying_app_success"]
    APP_ACKNOWLEDGEMENT_FIELD_NUMBER: _ClassVar[int]
    FORWARD_RELAYER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UNDERLYING_APP_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    app_acknowledgement: bytes
    forward_relayer_address: str
    underlying_app_success: bool
    def __init__(self, app_acknowledgement: _Optional[bytes] = ..., forward_relayer_address: _Optional[str] = ..., underlying_app_success: bool = ...) -> None: ...
