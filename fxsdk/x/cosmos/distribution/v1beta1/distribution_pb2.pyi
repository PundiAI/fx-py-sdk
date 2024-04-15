from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ["community_tax", "base_proposer_reward", "bonus_proposer_reward", "withdraw_addr_enabled"]
    COMMUNITY_TAX_FIELD_NUMBER: _ClassVar[int]
    BASE_PROPOSER_REWARD_FIELD_NUMBER: _ClassVar[int]
    BONUS_PROPOSER_REWARD_FIELD_NUMBER: _ClassVar[int]
    WITHDRAW_ADDR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    community_tax: str
    base_proposer_reward: str
    bonus_proposer_reward: str
    withdraw_addr_enabled: bool
    def __init__(self, community_tax: _Optional[str] = ..., base_proposer_reward: _Optional[str] = ..., bonus_proposer_reward: _Optional[str] = ..., withdraw_addr_enabled: bool = ...) -> None: ...

class ValidatorHistoricalRewards(_message.Message):
    __slots__ = ["cumulative_reward_ratio", "reference_count"]
    CUMULATIVE_REWARD_RATIO_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    cumulative_reward_ratio: _containers.RepeatedCompositeFieldContainer[_coin_pb2.DecCoin]
    reference_count: int
    def __init__(self, cumulative_reward_ratio: _Optional[_Iterable[_Union[_coin_pb2.DecCoin, _Mapping]]] = ..., reference_count: _Optional[int] = ...) -> None: ...

class ValidatorCurrentRewards(_message.Message):
    __slots__ = ["rewards", "period"]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    rewards: _containers.RepeatedCompositeFieldContainer[_coin_pb2.DecCoin]
    period: int
    def __init__(self, rewards: _Optional[_Iterable[_Union[_coin_pb2.DecCoin, _Mapping]]] = ..., period: _Optional[int] = ...) -> None: ...

class ValidatorAccumulatedCommission(_message.Message):
    __slots__ = ["commission"]
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    commission: _containers.RepeatedCompositeFieldContainer[_coin_pb2.DecCoin]
    def __init__(self, commission: _Optional[_Iterable[_Union[_coin_pb2.DecCoin, _Mapping]]] = ...) -> None: ...

class ValidatorOutstandingRewards(_message.Message):
    __slots__ = ["rewards"]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    rewards: _containers.RepeatedCompositeFieldContainer[_coin_pb2.DecCoin]
    def __init__(self, rewards: _Optional[_Iterable[_Union[_coin_pb2.DecCoin, _Mapping]]] = ...) -> None: ...

class ValidatorSlashEvent(_message.Message):
    __slots__ = ["validator_period", "fraction"]
    VALIDATOR_PERIOD_FIELD_NUMBER: _ClassVar[int]
    FRACTION_FIELD_NUMBER: _ClassVar[int]
    validator_period: int
    fraction: str
    def __init__(self, validator_period: _Optional[int] = ..., fraction: _Optional[str] = ...) -> None: ...

class ValidatorSlashEvents(_message.Message):
    __slots__ = ["validator_slash_events"]
    VALIDATOR_SLASH_EVENTS_FIELD_NUMBER: _ClassVar[int]
    validator_slash_events: _containers.RepeatedCompositeFieldContainer[ValidatorSlashEvent]
    def __init__(self, validator_slash_events: _Optional[_Iterable[_Union[ValidatorSlashEvent, _Mapping]]] = ...) -> None: ...

class FeePool(_message.Message):
    __slots__ = ["community_pool"]
    COMMUNITY_POOL_FIELD_NUMBER: _ClassVar[int]
    community_pool: _containers.RepeatedCompositeFieldContainer[_coin_pb2.DecCoin]
    def __init__(self, community_pool: _Optional[_Iterable[_Union[_coin_pb2.DecCoin, _Mapping]]] = ...) -> None: ...

class CommunityPoolSpendProposal(_message.Message):
    __slots__ = ["title", "description", "recipient", "amount"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    recipient: str
    amount: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., recipient: _Optional[str] = ..., amount: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]] = ...) -> None: ...

class DelegatorStartingInfo(_message.Message):
    __slots__ = ["previous_period", "stake", "height"]
    PREVIOUS_PERIOD_FIELD_NUMBER: _ClassVar[int]
    STAKE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    previous_period: int
    stake: str
    height: int
    def __init__(self, previous_period: _Optional[int] = ..., stake: _Optional[str] = ..., height: _Optional[int] = ...) -> None: ...

class DelegationDelegatorReward(_message.Message):
    __slots__ = ["validator_address", "reward"]
    VALIDATOR_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    validator_address: str
    reward: _containers.RepeatedCompositeFieldContainer[_coin_pb2.DecCoin]
    def __init__(self, validator_address: _Optional[str] = ..., reward: _Optional[_Iterable[_Union[_coin_pb2.DecCoin, _Mapping]]] = ...) -> None: ...

class CommunityPoolSpendProposalWithDeposit(_message.Message):
    __slots__ = ["title", "description", "recipient", "amount", "deposit"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    recipient: str
    amount: str
    deposit: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., recipient: _Optional[str] = ..., amount: _Optional[str] = ..., deposit: _Optional[str] = ...) -> None: ...
