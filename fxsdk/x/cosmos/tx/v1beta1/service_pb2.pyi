from google.api import annotations_pb2 as _annotations_pb2
from fxsdk.x.cosmos.base.abci.v1beta1 import abci_pb2 as _abci_pb2
from fxsdk.x.cosmos.tx.v1beta1 import tx_pb2 as _tx_pb2
from fxsdk.x.cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from fxsdk.x.tendermint.types import block_pb2 as _block_pb2
from fxsdk.x.tendermint.types import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrderBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ORDER_BY_UNSPECIFIED: _ClassVar[OrderBy]
    ORDER_BY_ASC: _ClassVar[OrderBy]
    ORDER_BY_DESC: _ClassVar[OrderBy]

class BroadcastMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BROADCAST_MODE_UNSPECIFIED: _ClassVar[BroadcastMode]
    BROADCAST_MODE_BLOCK: _ClassVar[BroadcastMode]
    BROADCAST_MODE_SYNC: _ClassVar[BroadcastMode]
    BROADCAST_MODE_ASYNC: _ClassVar[BroadcastMode]
ORDER_BY_UNSPECIFIED: OrderBy
ORDER_BY_ASC: OrderBy
ORDER_BY_DESC: OrderBy
BROADCAST_MODE_UNSPECIFIED: BroadcastMode
BROADCAST_MODE_BLOCK: BroadcastMode
BROADCAST_MODE_SYNC: BroadcastMode
BROADCAST_MODE_ASYNC: BroadcastMode

class GetTxsEventRequest(_message.Message):
    __slots__ = ["events", "pagination", "order_by", "page", "limit"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedScalarFieldContainer[str]
    pagination: _pagination_pb2.PageRequest
    order_by: OrderBy
    page: int
    limit: int
    def __init__(self, events: _Optional[_Iterable[str]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ..., order_by: _Optional[_Union[OrderBy, str]] = ..., page: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class GetTxsEventResponse(_message.Message):
    __slots__ = ["txs", "tx_responses", "pagination", "total"]
    TXS_FIELD_NUMBER: _ClassVar[int]
    TX_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    txs: _containers.RepeatedCompositeFieldContainer[_tx_pb2.Tx]
    tx_responses: _containers.RepeatedCompositeFieldContainer[_abci_pb2.TxResponse]
    pagination: _pagination_pb2.PageResponse
    total: int
    def __init__(self, txs: _Optional[_Iterable[_Union[_tx_pb2.Tx, _Mapping]]] = ..., tx_responses: _Optional[_Iterable[_Union[_abci_pb2.TxResponse, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ..., total: _Optional[int] = ...) -> None: ...

class BroadcastTxRequest(_message.Message):
    __slots__ = ["tx_bytes", "mode"]
    TX_BYTES_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    tx_bytes: bytes
    mode: BroadcastMode
    def __init__(self, tx_bytes: _Optional[bytes] = ..., mode: _Optional[_Union[BroadcastMode, str]] = ...) -> None: ...

class BroadcastTxResponse(_message.Message):
    __slots__ = ["tx_response"]
    TX_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    tx_response: _abci_pb2.TxResponse
    def __init__(self, tx_response: _Optional[_Union[_abci_pb2.TxResponse, _Mapping]] = ...) -> None: ...

class SimulateRequest(_message.Message):
    __slots__ = ["tx", "tx_bytes"]
    TX_FIELD_NUMBER: _ClassVar[int]
    TX_BYTES_FIELD_NUMBER: _ClassVar[int]
    tx: _tx_pb2.Tx
    tx_bytes: bytes
    def __init__(self, tx: _Optional[_Union[_tx_pb2.Tx, _Mapping]] = ..., tx_bytes: _Optional[bytes] = ...) -> None: ...

class SimulateResponse(_message.Message):
    __slots__ = ["gas_info", "result"]
    GAS_INFO_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    gas_info: _abci_pb2.GasInfo
    result: _abci_pb2.Result
    def __init__(self, gas_info: _Optional[_Union[_abci_pb2.GasInfo, _Mapping]] = ..., result: _Optional[_Union[_abci_pb2.Result, _Mapping]] = ...) -> None: ...

class GetTxRequest(_message.Message):
    __slots__ = ["hash"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class GetTxResponse(_message.Message):
    __slots__ = ["tx", "tx_response"]
    TX_FIELD_NUMBER: _ClassVar[int]
    TX_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    tx: _tx_pb2.Tx
    tx_response: _abci_pb2.TxResponse
    def __init__(self, tx: _Optional[_Union[_tx_pb2.Tx, _Mapping]] = ..., tx_response: _Optional[_Union[_abci_pb2.TxResponse, _Mapping]] = ...) -> None: ...

class GetBlockWithTxsRequest(_message.Message):
    __slots__ = ["height", "pagination"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    height: int
    pagination: _pagination_pb2.PageRequest
    def __init__(self, height: _Optional[int] = ..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class GetBlockWithTxsResponse(_message.Message):
    __slots__ = ["txs", "block_id", "block", "pagination"]
    TXS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    txs: _containers.RepeatedCompositeFieldContainer[_tx_pb2.Tx]
    block_id: _types_pb2.BlockID
    block: _block_pb2.Block
    pagination: _pagination_pb2.PageResponse
    def __init__(self, txs: _Optional[_Iterable[_Union[_tx_pb2.Tx, _Mapping]]] = ..., block_id: _Optional[_Union[_types_pb2.BlockID, _Mapping]] = ..., block: _Optional[_Union[_block_pb2.Block, _Mapping]] = ..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]] = ...) -> None: ...
