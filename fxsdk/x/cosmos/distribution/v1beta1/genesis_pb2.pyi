from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from cosmos.distribution.v1beta1 import distribution_pb2 as _distribution_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DelegatorWithdrawInfo(_message.Message):
    __slots__ = ["delegator_address", "withdraw_address"]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    WITHDRAW_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    withdraw_address: str
    def __init__(self, delegator_address: _Optional[str] = ..., withdraw_address: _Optional[str] = ...) -> None: ...

class ValidatorOutstandingRewardsRecord(_message.Message):
    __slots__ = ["validator_address", "outstanding_rewards"]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OUTSTANDING_REWARDS_FIELD_NUMBER: _ClassVar[int]
    validator_address: str
    outstanding_rewards: _containers.RepeatedCompositeFieldContainer[_coin_pb2.DecCoin]
    def __init__(self, validator_address: _Optional[str] = ..., outstanding_rewards: _Optional[_Iterable[_Union[_coin_pb2.DecCoin, _Mapping]]] = ...) -> None: ...

class ValidatorAccumulatedCommissionRecord(_message.Message):
    __slots__ = ["validator_address", "accumulated"]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ACCUMULATED_FIELD_NUMBER: _ClassVar[int]
    validator_address: str
    accumulated: _distribution_pb2.ValidatorAccumulatedCommission
    def __init__(self, validator_address: _Optional[str] = ..., accumulated: _Optional[_Union[_distribution_pb2.ValidatorAccumulatedCommission, _Mapping]] = ...) -> None: ...

class ValidatorHistoricalRewardsRecord(_message.Message):
    __slots__ = ["validator_address", "period", "rewards"]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    validator_address: str
    period: int
    rewards: _distribution_pb2.ValidatorHistoricalRewards
    def __init__(self, validator_address: _Optional[str] = ..., period: _Optional[int] = ..., rewards: _Optional[_Union[_distribution_pb2.ValidatorHistoricalRewards, _Mapping]] = ...) -> None: ...

class ValidatorCurrentRewardsRecord(_message.Message):
    __slots__ = ["validator_address", "rewards"]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    validator_address: str
    rewards: _distribution_pb2.ValidatorCurrentRewards
    def __init__(self, validator_address: _Optional[str] = ..., rewards: _Optional[_Union[_distribution_pb2.ValidatorCurrentRewards, _Mapping]] = ...) -> None: ...

class DelegatorStartingInfoRecord(_message.Message):
    __slots__ = ["delegator_address", "validator_address", "starting_info"]
    DELEGATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STARTING_INFO_FIELD_NUMBER: _ClassVar[int]
    delegator_address: str
    validator_address: str
    starting_info: _distribution_pb2.DelegatorStartingInfo
    def __init__(self, delegator_address: _Optional[str] = ..., validator_address: _Optional[str] = ..., starting_info: _Optional[_Union[_distribution_pb2.DelegatorStartingInfo, _Mapping]] = ...) -> None: ...

class ValidatorSlashEventRecord(_message.Message):
    __slots__ = ["validator_address", "height", "period", "validator_slash_event"]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_SLASH_EVENT_FIELD_NUMBER: _ClassVar[int]
    validator_address: str
    height: int
    period: int
    validator_slash_event: _distribution_pb2.ValidatorSlashEvent
    def __init__(self, validator_address: _Optional[str] = ..., height: _Optional[int] = ..., period: _Optional[int] = ..., validator_slash_event: _Optional[_Union[_distribution_pb2.ValidatorSlashEvent, _Mapping]] = ...) -> None: ...

class GenesisState(_message.Message):
    __slots__ = ["params", "fee_pool", "delegator_withdraw_infos", "previous_proposer", "outstanding_rewards", "validator_accumulated_commissions", "validator_historical_rewards", "validator_current_rewards", "delegator_starting_infos", "validator_slash_events"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    FEE_POOL_FIELD_NUMBER: _ClassVar[int]
    DELEGATOR_WITHDRAW_INFOS_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_PROPOSER_FIELD_NUMBER: _ClassVar[int]
    OUTSTANDING_REWARDS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ACCUMULATED_COMMISSIONS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_HISTORICAL_REWARDS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_CURRENT_REWARDS_FIELD_NUMBER: _ClassVar[int]
    DELEGATOR_STARTING_INFOS_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_SLASH_EVENTS_FIELD_NUMBER: _ClassVar[int]
    params: _distribution_pb2.Params
    fee_pool: _distribution_pb2.FeePool
    delegator_withdraw_infos: _containers.RepeatedCompositeFieldContainer[DelegatorWithdrawInfo]
    previous_proposer: str
    outstanding_rewards: _containers.RepeatedCompositeFieldContainer[ValidatorOutstandingRewardsRecord]
    validator_accumulated_commissions: _containers.RepeatedCompositeFieldContainer[ValidatorAccumulatedCommissionRecord]
    validator_historical_rewards: _containers.RepeatedCompositeFieldContainer[ValidatorHistoricalRewardsRecord]
    validator_current_rewards: _containers.RepeatedCompositeFieldContainer[ValidatorCurrentRewardsRecord]
    delegator_starting_infos: _containers.RepeatedCompositeFieldContainer[DelegatorStartingInfoRecord]
    validator_slash_events: _containers.RepeatedCompositeFieldContainer[ValidatorSlashEventRecord]
    def __init__(self, params: _Optional[_Union[_distribution_pb2.Params, _Mapping]] = ..., fee_pool: _Optional[_Union[_distribution_pb2.FeePool, _Mapping]] = ..., delegator_withdraw_infos: _Optional[_Iterable[_Union[DelegatorWithdrawInfo, _Mapping]]] = ..., previous_proposer: _Optional[str] = ..., outstanding_rewards: _Optional[_Iterable[_Union[ValidatorOutstandingRewardsRecord, _Mapping]]] = ..., validator_accumulated_commissions: _Optional[_Iterable[_Union[ValidatorAccumulatedCommissionRecord, _Mapping]]] = ..., validator_historical_rewards: _Optional[_Iterable[_Union[ValidatorHistoricalRewardsRecord, _Mapping]]] = ..., validator_current_rewards: _Optional[_Iterable[_Union[ValidatorCurrentRewardsRecord, _Mapping]]] = ..., delegator_starting_infos: _Optional[_Iterable[_Union[DelegatorStartingInfoRecord, _Mapping]]] = ..., validator_slash_events: _Optional[_Iterable[_Union[ValidatorSlashEventRecord, _Mapping]]] = ...) -> None: ...
