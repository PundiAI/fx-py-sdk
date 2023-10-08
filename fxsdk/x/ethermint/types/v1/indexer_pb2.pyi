from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TxResult(_message.Message):
    __slots__ = ["height", "tx_index", "msg_index", "eth_tx_index", "failed", "gas_used", "cumulative_gas_used"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TX_INDEX_FIELD_NUMBER: _ClassVar[int]
    MSG_INDEX_FIELD_NUMBER: _ClassVar[int]
    ETH_TX_INDEX_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    GAS_USED_FIELD_NUMBER: _ClassVar[int]
    CUMULATIVE_GAS_USED_FIELD_NUMBER: _ClassVar[int]
    height: int
    tx_index: int
    msg_index: int
    eth_tx_index: int
    failed: bool
    gas_used: int
    cumulative_gas_used: int
    def __init__(self, height: _Optional[int] = ..., tx_index: _Optional[int] = ..., msg_index: _Optional[int] = ..., eth_tx_index: _Optional[int] = ..., failed: bool = ..., gas_used: _Optional[int] = ..., cumulative_gas_used: _Optional[int] = ...) -> None: ...
