from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ["evm_denom", "enable_create", "enable_call", "extra_eips", "chain_config", "allow_unprotected_txs"]
    EVM_DENOM_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CREATE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CALL_FIELD_NUMBER: _ClassVar[int]
    EXTRA_EIPS_FIELD_NUMBER: _ClassVar[int]
    CHAIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ALLOW_UNPROTECTED_TXS_FIELD_NUMBER: _ClassVar[int]
    evm_denom: str
    enable_create: bool
    enable_call: bool
    extra_eips: _containers.RepeatedScalarFieldContainer[int]
    chain_config: ChainConfig
    allow_unprotected_txs: bool
    def __init__(self, evm_denom: _Optional[str] = ..., enable_create: bool = ..., enable_call: bool = ..., extra_eips: _Optional[_Iterable[int]] = ..., chain_config: _Optional[_Union[ChainConfig, _Mapping]] = ..., allow_unprotected_txs: bool = ...) -> None: ...

class ChainConfig(_message.Message):
    __slots__ = ["homestead_block", "dao_fork_block", "dao_fork_support", "eip150_block", "eip150_hash", "eip155_block", "eip158_block", "byzantium_block", "constantinople_block", "petersburg_block", "istanbul_block", "muir_glacier_block", "berlin_block", "london_block", "arrow_glacier_block", "gray_glacier_block", "merge_netsplit_block", "shanghai_block", "cancun_block"]
    HOMESTEAD_BLOCK_FIELD_NUMBER: _ClassVar[int]
    DAO_FORK_BLOCK_FIELD_NUMBER: _ClassVar[int]
    DAO_FORK_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    EIP150_BLOCK_FIELD_NUMBER: _ClassVar[int]
    EIP150_HASH_FIELD_NUMBER: _ClassVar[int]
    EIP155_BLOCK_FIELD_NUMBER: _ClassVar[int]
    EIP158_BLOCK_FIELD_NUMBER: _ClassVar[int]
    BYZANTIUM_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CONSTANTINOPLE_BLOCK_FIELD_NUMBER: _ClassVar[int]
    PETERSBURG_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ISTANBUL_BLOCK_FIELD_NUMBER: _ClassVar[int]
    MUIR_GLACIER_BLOCK_FIELD_NUMBER: _ClassVar[int]
    BERLIN_BLOCK_FIELD_NUMBER: _ClassVar[int]
    LONDON_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ARROW_GLACIER_BLOCK_FIELD_NUMBER: _ClassVar[int]
    GRAY_GLACIER_BLOCK_FIELD_NUMBER: _ClassVar[int]
    MERGE_NETSPLIT_BLOCK_FIELD_NUMBER: _ClassVar[int]
    SHANGHAI_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CANCUN_BLOCK_FIELD_NUMBER: _ClassVar[int]
    homestead_block: str
    dao_fork_block: str
    dao_fork_support: bool
    eip150_block: str
    eip150_hash: str
    eip155_block: str
    eip158_block: str
    byzantium_block: str
    constantinople_block: str
    petersburg_block: str
    istanbul_block: str
    muir_glacier_block: str
    berlin_block: str
    london_block: str
    arrow_glacier_block: str
    gray_glacier_block: str
    merge_netsplit_block: str
    shanghai_block: str
    cancun_block: str
    def __init__(self, homestead_block: _Optional[str] = ..., dao_fork_block: _Optional[str] = ..., dao_fork_support: bool = ..., eip150_block: _Optional[str] = ..., eip150_hash: _Optional[str] = ..., eip155_block: _Optional[str] = ..., eip158_block: _Optional[str] = ..., byzantium_block: _Optional[str] = ..., constantinople_block: _Optional[str] = ..., petersburg_block: _Optional[str] = ..., istanbul_block: _Optional[str] = ..., muir_glacier_block: _Optional[str] = ..., berlin_block: _Optional[str] = ..., london_block: _Optional[str] = ..., arrow_glacier_block: _Optional[str] = ..., gray_glacier_block: _Optional[str] = ..., merge_netsplit_block: _Optional[str] = ..., shanghai_block: _Optional[str] = ..., cancun_block: _Optional[str] = ...) -> None: ...

class State(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class TransactionLogs(_message.Message):
    __slots__ = ["hash", "logs"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    hash: str
    logs: _containers.RepeatedCompositeFieldContainer[Log]
    def __init__(self, hash: _Optional[str] = ..., logs: _Optional[_Iterable[_Union[Log, _Mapping]]] = ...) -> None: ...

class Log(_message.Message):
    __slots__ = ["address", "topics", "data", "block_number", "tx_hash", "tx_index", "block_hash", "index", "removed"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    BLOCK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TX_HASH_FIELD_NUMBER: _ClassVar[int]
    TX_INDEX_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    address: str
    topics: _containers.RepeatedScalarFieldContainer[str]
    data: bytes
    block_number: int
    tx_hash: str
    tx_index: int
    block_hash: str
    index: int
    removed: bool
    def __init__(self, address: _Optional[str] = ..., topics: _Optional[_Iterable[str]] = ..., data: _Optional[bytes] = ..., block_number: _Optional[int] = ..., tx_hash: _Optional[str] = ..., tx_index: _Optional[int] = ..., block_hash: _Optional[str] = ..., index: _Optional[int] = ..., removed: bool = ...) -> None: ...

class TxResult(_message.Message):
    __slots__ = ["contract_address", "bloom", "tx_logs", "ret", "reverted", "gas_used"]
    CONTRACT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BLOOM_FIELD_NUMBER: _ClassVar[int]
    TX_LOGS_FIELD_NUMBER: _ClassVar[int]
    RET_FIELD_NUMBER: _ClassVar[int]
    REVERTED_FIELD_NUMBER: _ClassVar[int]
    GAS_USED_FIELD_NUMBER: _ClassVar[int]
    contract_address: str
    bloom: bytes
    tx_logs: TransactionLogs
    ret: bytes
    reverted: bool
    gas_used: int
    def __init__(self, contract_address: _Optional[str] = ..., bloom: _Optional[bytes] = ..., tx_logs: _Optional[_Union[TransactionLogs, _Mapping]] = ..., ret: _Optional[bytes] = ..., reverted: bool = ..., gas_used: _Optional[int] = ...) -> None: ...

class AccessTuple(_message.Message):
    __slots__ = ["address", "storage_keys"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_KEYS_FIELD_NUMBER: _ClassVar[int]
    address: str
    storage_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, address: _Optional[str] = ..., storage_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class TraceConfig(_message.Message):
    __slots__ = ["tracer", "timeout", "reexec", "disable_stack", "disable_storage", "debug", "limit", "overrides", "enable_memory", "enable_return_data", "tracer_json_config"]
    TRACER_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    REEXEC_FIELD_NUMBER: _ClassVar[int]
    DISABLE_STACK_FIELD_NUMBER: _ClassVar[int]
    DISABLE_STORAGE_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MEMORY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RETURN_DATA_FIELD_NUMBER: _ClassVar[int]
    TRACER_JSON_CONFIG_FIELD_NUMBER: _ClassVar[int]
    tracer: str
    timeout: str
    reexec: int
    disable_stack: bool
    disable_storage: bool
    debug: bool
    limit: int
    overrides: ChainConfig
    enable_memory: bool
    enable_return_data: bool
    tracer_json_config: str
    def __init__(self, tracer: _Optional[str] = ..., timeout: _Optional[str] = ..., reexec: _Optional[int] = ..., disable_stack: bool = ..., disable_storage: bool = ..., debug: bool = ..., limit: _Optional[int] = ..., overrides: _Optional[_Union[ChainConfig, _Mapping]] = ..., enable_memory: bool = ..., enable_return_data: bool = ..., tracer_json_config: _Optional[str] = ...) -> None: ...
