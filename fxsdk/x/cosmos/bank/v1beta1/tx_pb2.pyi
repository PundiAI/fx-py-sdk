from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxpysdk.fxsdk.x.cosmos.bank.v1beta1 import bank_pb2 as _bank_pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxpysdk.fxsdk.x.cosmos.msg.v1 import msg_pb2 as _msg_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgSend(_message.Message):
    __slots__ = ["from_address", "to_address", "amount"]
    FROM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    from_address: str
    to_address: str
    amount: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, from_address: _Optional[str] = ..., to_address: _Optional[str] = ..., amount: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...

class MsgSendResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgMultiSend(_message.Message):
    __slots__ = ["inputs", "outputs"]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: _containers.RepeatedCompositeFieldContainer[_bank_pb2.Input]
    outputs: _containers.RepeatedCompositeFieldContainer[_bank_pb2.Output]
    def __init__(self, inputs: _Optional[_Iterable[_Union[_bank_pb2.Input, _Mapping]]] = ..., outputs: _Optional[_Iterable[_Union[_bank_pb2.Output, _Mapping]]] = ...) -> None: ...

class MsgMultiSendResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
