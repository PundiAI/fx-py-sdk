from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from fxpysdk.fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxpysdk.fxsdk.x.cosmos.staking.v1beta1 import staking_pb2 as _staking_pb2
from fxpysdk.fxsdk.x.cosmos.msg.v1 import msg_pb2 as _msg_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgCreateValidator(_message.Message):
    __slots__ = ["description", "commission", "min_self_delegation", "delegator_address", "validator_address", "pubkey", "value"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    MIN_SELF_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    description: _staking_pb2.Description
    commission: _staking_pb2.CommissionRates
    min_self_delegation: str
    delegator_address: str
    validator_address: str
    pubkey: _any_pb2.Any
    value: _coin_pb2.Coin
    def __init__(self, description: _Optional[_Union[_staking_pb2.Description, _Mapping]] = ..., commission: _Optional[_Union[_staking_pb2.CommissionRates, _Mapping]] = ..., min_self_delegation: _Optional[str] = ..., delegator_address: _Optional[str] = ..., validator_address: _Optional[str] = ..., pubkey: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., value: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ...) -> None: ...

class MsgCreateValidatorResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgEditValidator(_message.Message):
    __slots__ = ["description", "validator_address", "commission_rate", "min_self_delegation"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_RATE_FIELD_NUMBER: _ClassVar[int]
    MIN_SELF_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    description: _staking_pb2.Description
    validator_address: str
    commission_rate: str
    min_self_delegation: str
    def __init__(self, description: _Optional[_Union[_staking_pb2.Description, _Mapping]] = ..., validator_address: _Optional[str] = ..., commission_rate: _Optional[str] = ..., min_self_delegation: _Optional[str] = ...) -> None: ...

class MsgEditValidatorResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgDelegate(_message.Message):
    __slots__ = ["delegator_address", "validator_address", "amount"]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    validator_address: str
    amount: _coin_pb2.Coin
    def __init__(self, delegator_address: _Optional[str] = ..., validator_address: _Optional[str] = ..., amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ...) -> None: ...

class MsgDelegateResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MsgBeginRedelegate(_message.Message):
    __slots__ = ["delegator_address", "validator_src_address", "validator_dst_address", "amount"]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_SRC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_DST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    validator_src_address: str
    validator_dst_address: str
    amount: _coin_pb2.Coin
    def __init__(self, delegator_address: _Optional[str] = ..., validator_src_address: _Optional[str] = ..., validator_dst_address: _Optional[str] = ..., amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ...) -> None: ...

class MsgBeginRedelegateResponse(_message.Message):
    __slots__ = ["completion_time"]
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    completion_time: _timestamp_pb2.Timestamp
    def __init__(self, completion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MsgUndelegate(_message.Message):
    __slots__ = ["delegator_address", "validator_address", "amount"]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    validator_address: str
    amount: _coin_pb2.Coin
    def __init__(self, delegator_address: _Optional[str] = ..., validator_address: _Optional[str] = ..., amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ...) -> None: ...

class MsgUndelegateResponse(_message.Message):
    __slots__ = ["completion_time"]
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    completion_time: _timestamp_pb2.Timestamp
    def __init__(self, completion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MsgCancelUnbondingDelegation(_message.Message):
    __slots__ = ["delegator_address", "validator_address", "amount", "creation_height"]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CREATION_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    validator_address: str
    amount: _coin_pb2.Coin
    creation_height: int
    def __init__(self, delegator_address: _Optional[str] = ..., validator_address: _Optional[str] = ..., amount: _Optional[_Union[_coin_pb2.Coin, _Mapping]] = ..., creation_height: _Optional[int] = ...) -> None: ...

class MsgCancelUnbondingDelegationResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
