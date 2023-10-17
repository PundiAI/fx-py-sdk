from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxsdk.x.cosmos.auth.v1beta1 import auth_pb2 as _auth_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BaseVestingAccount(_message.Message):
    __slots__ = ["base_account", "original_vesting", "delegated_free", "delegated_vesting", "end_time"]
    BASE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_VESTING_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_FREE_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_VESTING_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    base_account: _auth_pb2.BaseAccount
    original_vesting: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    delegated_free: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    delegated_vesting: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    end_time: int
    def __init__(self, base_account: _Optional[_Union[_auth_pb2.BaseAccount, _Mapping]] = ..., original_vesting: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., delegated_free: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., delegated_vesting: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., end_time: _Optional[int] = ...) -> None: ...

class ContinuousVestingAccount(_message.Message):
    __slots__ = ["base_vesting_account", "start_time"]
    BASE_VESTING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    base_vesting_account: BaseVestingAccount
    start_time: int
    def __init__(self, base_vesting_account: _Optional[_Union[BaseVestingAccount, _Mapping]] = ..., start_time: _Optional[int] = ...) -> None: ...

class DelayedVestingAccount(_message.Message):
    __slots__ = ["base_vesting_account"]
    BASE_VESTING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    base_vesting_account: BaseVestingAccount
    def __init__(self, base_vesting_account: _Optional[_Union[BaseVestingAccount, _Mapping]] = ...) -> None: ...

class Period(_message.Message):
    __slots__ = ["length", "amount"]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    length: int
    amount: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, length: _Optional[int] = ..., amount: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...

class PeriodicVestingAccount(_message.Message):
    __slots__ = ["base_vesting_account", "start_time", "vesting_periods"]
    BASE_VESTING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    VESTING_PERIODS_FIELD_NUMBER: _ClassVar[int]
    base_vesting_account: BaseVestingAccount
    start_time: int
    vesting_periods: _containers.RepeatedCompositeFieldContainer[Period]
    def __init__(self, base_vesting_account: _Optional[_Union[BaseVestingAccount, _Mapping]] = ..., start_time: _Optional[int] = ..., vesting_periods: _Optional[_Iterable[_Union[Period, _Mapping]]] = ...) -> None: ...

class PermanentLockedAccount(_message.Message):
    __slots__ = ["base_vesting_account"]
    BASE_VESTING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    base_vesting_account: BaseVestingAccount
    def __init__(self, base_vesting_account: _Optional[_Union[BaseVestingAccount, _Mapping]] = ...) -> None: ...
