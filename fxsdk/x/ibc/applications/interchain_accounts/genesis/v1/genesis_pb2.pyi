from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as _gogo_pb2
from fxpysdk.fxsdk.x.ibc.applications.interchain_accounts.controller.v1 import controller_pb2 as _controller_pb2
from fxpysdk.fxsdk.x.ibc.applications.interchain_accounts.host.v1 import host_pb2 as _host_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ["controller_genesis_state", "host_genesis_state"]
    CONTROLLER_GENESIS_STATE_FIELD_NUMBER: _ClassVar[int]
    HOST_GENESIS_STATE_FIELD_NUMBER: _ClassVar[int]
    controller_genesis_state: ControllerGenesisState
    host_genesis_state: HostGenesisState
    def __init__(self, controller_genesis_state: _Optional[_Union[ControllerGenesisState, _Mapping]] = ..., host_genesis_state: _Optional[_Union[HostGenesisState, _Mapping]] = ...) -> None: ...

class ControllerGenesisState(_message.Message):
    __slots__ = ["active_channels", "interchain_accounts", "ports", "params"]
    ACTIVE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    INTERCHAIN_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    active_channels: _containers.RepeatedCompositeFieldContainer[ActiveChannel]
    interchain_accounts: _containers.RepeatedCompositeFieldContainer[RegisteredInterchainAccount]
    ports: _containers.RepeatedScalarFieldContainer[str]
    params: _controller_pb2.Params
    def __init__(self, active_channels: _Optional[_Iterable[_Union[ActiveChannel, _Mapping]]] = ..., interchain_accounts: _Optional[_Iterable[_Union[RegisteredInterchainAccount, _Mapping]]] = ..., ports: _Optional[_Iterable[str]] = ..., params: _Optional[_Union[_controller_pb2.Params, _Mapping]] = ...) -> None: ...

class HostGenesisState(_message.Message):
    __slots__ = ["active_channels", "interchain_accounts", "port", "params"]
    ACTIVE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    INTERCHAIN_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    active_channels: _containers.RepeatedCompositeFieldContainer[ActiveChannel]
    interchain_accounts: _containers.RepeatedCompositeFieldContainer[RegisteredInterchainAccount]
    port: str
    params: _host_pb2.Params
    def __init__(self, active_channels: _Optional[_Iterable[_Union[ActiveChannel, _Mapping]]] = ..., interchain_accounts: _Optional[_Iterable[_Union[RegisteredInterchainAccount, _Mapping]]] = ..., port: _Optional[str] = ..., params: _Optional[_Union[_host_pb2.Params, _Mapping]] = ...) -> None: ...

class ActiveChannel(_message.Message):
    __slots__ = ["connection_id", "port_id", "channel_id", "is_middleware_enabled"]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_MIDDLEWARE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    port_id: str
    channel_id: str
    is_middleware_enabled: bool
    def __init__(self, connection_id: _Optional[str] = ..., port_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., is_middleware_enabled: bool = ...) -> None: ...

class RegisteredInterchainAccount(_message.Message):
    __slots__ = ["connection_id", "port_id", "account_address"]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    port_id: str
    account_address: str
    def __init__(self, connection_id: _Optional[str] = ..., port_id: _Optional[str] = ..., account_address: _Optional[str] = ...) -> None: ...
