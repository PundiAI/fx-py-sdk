# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/evm/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxsdk.x.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from fxsdk.x.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x66x/evm/v1/tx.proto\x12\tfx.evm.v1\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\"v\n\x0fMsgCallContract\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x18\n\x10\x63ontract_address\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t:\x0e\x82\xe7\xb0*\tauthority\"\x19\n\x17MsgCallContractResponse2U\n\x03Msg\x12N\n\x0c\x43\x61llContract\x12\x1a.fx.evm.v1.MsgCallContract\x1a\".fx.evm.v1.MsgCallContractResponseB*Z(github.com/functionx/fx-core/x/evm/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fx.evm.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z(github.com/functionx/fx-core/x/evm/types'
  _MSGCALLCONTRACT.fields_by_name['authority']._options = None
  _MSGCALLCONTRACT.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGCALLCONTRACT._options = None
  _MSGCALLCONTRACT._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSGCALLCONTRACT']._serialized_start=85
  _globals['_MSGCALLCONTRACT']._serialized_end=203
  _globals['_MSGCALLCONTRACTRESPONSE']._serialized_start=205
  _globals['_MSGCALLCONTRACTRESPONSE']._serialized_end=230
  _globals['_MSG']._serialized_start=232
  _globals['_MSG']._serialized_end=317
# @@protoc_insertion_point(module_scope)