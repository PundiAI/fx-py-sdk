from google.api import annotations_pb2 as _annotations_pb2
from cosmos.upgrade.v1beta1 import upgrade_pb2 as _upgrade_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryCurrentPlanRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryCurrentPlanResponse(_message.Message):
    __slots__ = ["plan"]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    plan: _upgrade_pb2.Plan
    def __init__(self, plan: _Optional[_Union[_upgrade_pb2.Plan, _Mapping]] = ...) -> None: ...

class QueryAppliedPlanRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class QueryAppliedPlanResponse(_message.Message):
    __slots__ = ["height"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    height: int
    def __init__(self, height: _Optional[int] = ...) -> None: ...

class QueryUpgradedConsensusStateRequest(_message.Message):
    __slots__ = ["last_height"]
    LAST_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    last_height: int
    def __init__(self, last_height: _Optional[int] = ...) -> None: ...

class QueryUpgradedConsensusStateResponse(_message.Message):
    __slots__ = ["upgraded_consensus_state"]
    UPGRADED_CONSENSUS_STATE_FIELD_NUMBER: _ClassVar[int]
    upgraded_consensus_state: bytes
    def __init__(self, upgraded_consensus_state: _Optional[bytes] = ...) -> None: ...

class QueryModuleVersionsRequest(_message.Message):
    __slots__ = ["module_name"]
    MODULE_NAME_FIELD_NUMBER: _ClassVar[int]
    module_name: str
    def __init__(self, module_name: _Optional[str] = ...) -> None: ...

class QueryModuleVersionsResponse(_message.Message):
    __slots__ = ["module_versions"]
    MODULE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    module_versions: _containers.RepeatedCompositeFieldContainer[_upgrade_pb2.ModuleVersion]
    def __init__(self, module_versions: _Optional[_Iterable[_Union[_upgrade_pb2.ModuleVersion, _Mapping]]] = ...) -> None: ...

class QueryAuthorityRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryAuthorityResponse(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...
