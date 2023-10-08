from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FungibleTokenPacketData(_message.Message):
    __slots__ = ["denom", "amount", "sender", "receiver", "router", "fee", "memo"]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    ROUTER_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    denom: str
    amount: str
    sender: str
    receiver: str
    router: str
    fee: str
    memo: str
    def __init__(self, denom: _Optional[str] = ..., amount: _Optional[str] = ..., sender: _Optional[str] = ..., receiver: _Optional[str] = ..., router: _Optional[str] = ..., fee: _Optional[str] = ..., memo: _Optional[str] = ...) -> None: ...
