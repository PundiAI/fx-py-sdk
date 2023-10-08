from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from cosmos.vesting.v1beta1 import vesting_pb2 as _vesting_pb2
from cosmos.msg.v1 import msg_pb2 as _msg_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgCreateVestingAccount(_message.Message):
    __slots__ = ["from_address", "to_address", "amount", "end_time", "delayed"]
    FROM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    DELAYED_FIELD_NUMBER: _ClassVar[int]
    from_address: str
    to_address: str
    amount: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    end_time: int
    delayed: bool
    def __init__(self, from_address: _Optional[str] = ..., to_address: _Optional[str] = ..., amount: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., end_time: _Optional[int] = ..., delayed: bool = ...) -> None: ...

class MsgCreateVestingAccountResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgCreatePermanentLockedAccount(_message.Message):
    __slots__ = ["from_address", "to_address", "amount"]
    FROM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    from_address: str
    to_address: str
    amount: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, from_address: _Optional[str] = ..., to_address: _Optional[str] = ..., amount: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...

class MsgCreatePermanentLockedAccountResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgCreatePeriodicVestingAccount(_message.Message):
    __slots__ = ["from_address", "to_address", "start_time", "vesting_periods"]
    FROM_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    VESTING_PERIODS_FIELD_NUMBER: _ClassVar[int]
    from_address: str
    to_address: str
    start_time: int
    vesting_periods: _containers.RepeatedCompositeFieldContainer[_vesting_pb2.Period]
    def __init__(self, from_address: _Optional[str] = ..., to_address: _Optional[str] = ..., start_time: _Optional[int] = ..., vesting_periods: _Optional[_Iterable[_Union[_vesting_pb2.Period, _Mapping]]] = ...) -> None: ...

class MsgCreatePeriodicVestingAccountResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
