from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from cosmos.distribution.v1beta1 import distribution_pb2 as _distribution_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryParamsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryParamsResponse(_message.Message):
    __slots__ = ["params"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _distribution_pb2.Params
    def __init__(self, params: _Optional[_Union[_distribution_pb2.Params, _Mapping]] = ...) -> None: ...

class QueryValidatorOutstandingRewardsRequest(_message.Message):
    __slots__ = ["validator_address"]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    validator_address: str
    def __init__(self, validator_address: _Optional[str] = ...) -> None: ...

class QueryValidatorOutstandingRewardsResponse(_message.Message):
    __slots__ = ["rewards"]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    rewards: _distribution_pb2.ValidatorOutstandingRewards
    def __init__(self, rewards: _Optional[_Union[_distribution_pb2.ValidatorOutstandingRewards, _Mapping]] = ...) -> None: ...

class QueryValidatorCommissionRequest(_message.Message):
    __slots__ = ["validator_address"]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    validator_address: str
    def __init__(self, validator_address: _Optional[str] = ...) -> None: ...

class QueryValidatorCommissionResponse(_message.Message):
    __slots__ = ["commission"]
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    commission: _distribution_pb2.ValidatorAccumulatedCommission
    def __init__(self, commission: _Optional[_Union[_distribution_pb2.ValidatorAccumulatedCommission, _Mapping]] = ...) -> None: ...

class QueryValidatorSlashesRequest(_message.Message):
    __slots__ = ["validator_address", "starting_height", "ending_height", "pagination"]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STARTING_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ENDING_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    validator_address: str
    starting_height: int
    ending_height: int
    pagination: _pagination_pb2.PageRequest
    def __init__(self, validator_address: _Optional[str] = ..., starting_height: _Optional[int] = ..., ending_height: _Optional[int] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class QueryValidatorSlashesResponse(_message.Message):
    __slots__ = ["slashes", "pagination"]
    SLASHES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    slashes: _containers.RepeatedCompositeFieldContainer[_distribution_pb2.ValidatorSlashEvent]
    pagination: _pagination_pb2.PageResponse
    def __init__(self, slashes: _Optional[_Iterable[_Union[_distribution_pb2.ValidatorSlashEvent, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class QueryDelegationRewardsRequest(_message.Message):
    __slots__ = ["delegator_address", "validator_address"]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    validator_address: str
    def __init__(self, delegator_address: _Optional[str] = ..., validator_address: _Optional[str] = ...) -> None: ...

class QueryDelegationRewardsResponse(_message.Message):
    __slots__ = ["rewards"]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    rewards: _containers.RepeatedCompositeFieldContainer[_coin_pb2.DecCoin]
    def __init__(self, rewards: _Optional[_Iterable[_Union[_coin_pb2.DecCoin, _Mapping]]] = ...) -> None: ...

class QueryDelegationTotalRewardsRequest(_message.Message):
    __slots__ = ["delegator_address"]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    def __init__(self, delegator_address: _Optional[str] = ...) -> None: ...

class QueryDelegationTotalRewardsResponse(_message.Message):
    __slots__ = ["rewards", "total"]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    rewards: _containers.RepeatedCompositeFieldContainer[_distribution_pb2.DelegationDelegatorReward]
    total: _containers.RepeatedCompositeFieldContainer[_coin_pb2.DecCoin]
    def __init__(self, rewards: _Optional[_Iterable[_Union[_distribution_pb2.DelegationDelegatorReward, _Mapping]]] = ..., total: _Optional[_Iterable[_Union[_coin_pb2.DecCoin, _Mapping]]] = ...) -> None: ...

class QueryDelegatorValidatorsRequest(_message.Message):
    __slots__ = ["delegator_address"]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    def __init__(self, delegator_address: _Optional[str] = ...) -> None: ...

class QueryDelegatorValidatorsResponse(_message.Message):
    __slots__ = ["validators"]
    VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    validators: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, validators: _Optional[_Iterable[str]] = ...) -> None: ...

class QueryDelegatorWithdrawAddressRequest(_message.Message):
    __slots__ = ["delegator_address"]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    def __init__(self, delegator_address: _Optional[str] = ...) -> None: ...

class QueryDelegatorWithdrawAddressResponse(_message.Message):
    __slots__ = ["withdraw_address"]
    WITHDRAW_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    withdraw_address: str
    def __init__(self, withdraw_address: _Optional[str] = ...) -> None: ...

class QueryCommunityPoolRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryCommunityPoolResponse(_message.Message):
    __slots__ = ["pool"]
    POOL_FIELD_NUMBER: _ClassVar[int]
    pool: _containers.RepeatedCompositeFieldContainer[_coin_pb2.DecCoin]
    def __init__(self, pool: _Optional[_Iterable[_Union[_coin_pb2.DecCoin, _Mapping]]] = ...) -> None: ...
