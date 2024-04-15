from fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxsdk.x.fx.dex.v1 import funding_pb2 as _funding_pb2
from fxsdk.x.fx.dex.v1 import margin_pb2 as _margin_pb2
from fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResetFundingTimeProposal(_message.Message):
    __slots__ = ["title", "description", "funding_time"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FUNDING_TIME_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    funding_time: _funding_pb2.FundingTime
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., funding_time: _Optional[_Union[_funding_pb2.FundingTime, _Mapping]] = ...) -> None: ...

class ResetFundingParamsProposal(_message.Message):
    __slots__ = ["title", "description", "funding_params"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FUNDING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    funding_params: _funding_pb2.Funding
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., funding_params: _Optional[_Union[_funding_pb2.Funding, _Mapping]] = ...) -> None: ...

class ResetMMATableProposal(_message.Message):
    __slots__ = ["title", "description", "margin_rate_tables"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARGIN_RATE_TABLES_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    margin_rate_tables: _containers.RepeatedCompositeFieldContainer[_margin_pb2.MarginRateTable]
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., margin_rate_tables: _Optional[_Iterable[_Union[_margin_pb2.MarginRateTable, _Mapping]]] = ...) -> None: ...

class CreatePairProposal(_message.Message):
    __slots__ = ["title", "description", "pair"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    pair: Pair
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., pair: _Optional[_Union[Pair, _Mapping]] = ...) -> None: ...

class Pair(_message.Message):
    __slots__ = ["base_asset", "quote_asset", "market_status", "price_decimal", "position_decimal", "init_price", "market_type"]
    BASE_ASSET_FIELD_NUMBER: _ClassVar[int]
    QUOTE_ASSET_FIELD_NUMBER: _ClassVar[int]
    MARKET_STATUS_FIELD_NUMBER: _ClassVar[int]
    PRICE_DECIMAL_FIELD_NUMBER: _ClassVar[int]
    POSITION_DECIMAL_FIELD_NUMBER: _ClassVar[int]
    INIT_PRICE_FIELD_NUMBER: _ClassVar[int]
    MARKET_TYPE_FIELD_NUMBER: _ClassVar[int]
    base_asset: str
    quote_asset: str
    market_status: int
    price_decimal: int
    position_decimal: int
    init_price: str
    market_type: str
    def __init__(self, base_asset: _Optional[str] = ..., quote_asset: _Optional[str] = ..., market_status: _Optional[int] = ..., price_decimal: _Optional[int] = ..., position_decimal: _Optional[int] = ..., init_price: _Optional[str] = ..., market_type: _Optional[str] = ...) -> None: ...

class ResetPremiumIndexConfigProposal(_message.Message):
    __slots__ = ["title", "description", "premium_index_conf"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PREMIUM_INDEX_CONF_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    premium_index_conf: _funding_pb2.PremiumIndexConf
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., premium_index_conf: _Optional[_Union[_funding_pb2.PremiumIndexConf, _Mapping]] = ...) -> None: ...

class ShareSplitProposal(_message.Message):
    __slots__ = ["title", "description", "multiplier", "pair_id"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    multiplier: str
    pair_id: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., multiplier: _Optional[str] = ..., pair_id: _Optional[str] = ...) -> None: ...

class TradingFeeSpendProposal(_message.Message):
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

class TradingFeeSpendProposalWithDeposit(_message.Message):
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

class UnlistPairProposal(_message.Message):
    __slots__ = ["title", "description", "pair_id", "fee_receiver"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PAIR_ID_FIELD_NUMBER: _ClassVar[int]
    FEE_RECEIVER_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    pair_id: str
    fee_receiver: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., pair_id: _Optional[str] = ..., fee_receiver: _Optional[str] = ...) -> None: ...

class SendToFxcoreProposal(_message.Message):
    __slots__ = ["title", "description", "fee_receiver", "channel"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FEE_RECEIVER_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    fee_receiver: str
    channel: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., fee_receiver: _Optional[str] = ..., channel: _Optional[str] = ...) -> None: ...
