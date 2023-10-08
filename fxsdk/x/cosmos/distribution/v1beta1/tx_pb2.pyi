from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from cosmos.msg.v1 import msg_pb2 as _msg_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgSetWithdrawAddress(_message.Message):
    __slots__ = ["delegator_address", "withdraw_address"]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    WITHDRAW_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    withdraw_address: str
    def __init__(self, delegator_address: _Optional[str] = ..., withdraw_address: _Optional[str] = ...) -> None: ...

class MsgSetWithdrawAddressResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgWithdrawDelegatorReward(_message.Message):
    __slots__ = ["delegator_address", "validator_address"]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    validator_address: str
    def __init__(self, delegator_address: _Optional[str] = ..., validator_address: _Optional[str] = ...) -> None: ...

class MsgWithdrawDelegatorRewardResponse(_message.Message):
    __slots__ = ["amount"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    amount: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, amount: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...

class MsgWithdrawValidatorCommission(_message.Message):
    __slots__ = ["validator_address"]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    validator_address: str
    def __init__(self, validator_address: _Optional[str] = ...) -> None: ...

class MsgWithdrawValidatorCommissionResponse(_message.Message):
    __slots__ = ["amount"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    amount: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, amount: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...

class MsgFundCommunityPool(_message.Message):
    __slots__ = ["amount", "depositor"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DEPOSITOR_FIELD_NUMBER: _ClassVar[int]
    amount: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    depositor: str
    def __init__(self, amount: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ..., depositor: _Optional[str] = ...) -> None: ...

class MsgFundCommunityPoolResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
