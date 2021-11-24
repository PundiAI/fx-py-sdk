# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/erc20/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from x.cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from x.fx.erc20.v1 import erc20_pb2 as fx_dot_erc20_dot_v1_dot_erc20__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x66x/erc20/v1/genesis.proto\x12\x0b\x66x.erc20.v1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17\x66x/erc20/v1/erc20.proto\"l\n\x0cGenesisState\x12)\n\x06params\x18\x01 \x01(\x0b\x32\x13.fx.erc20.v1.ParamsB\x04\xc8\xde\x1f\x00\x12\x31\n\x0btoken_pairs\x18\x02 \x03(\x0b\x32\x16.fx.erc20.v1.TokenPairB\x04\xc8\xde\x1f\x00\"\xcd\x01\n\x06Params\x12-\n\x0c\x65nable_erc20\x18\x01 \x01(\x08\x42\x17\xf2\xde\x1f\x13yaml:\"enable_erc20\"\x12\x44\n\x0f\x65nable_evm_hook\x18\x02 \x01(\x08\x42+\xe2\xde\x1f\rEnableEVMHook\xf2\xde\x1f\x16yaml:\"enable_evm_hook\"\x12N\n\x0bibc_timeout\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\x1e\x98\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:\"ibc_timeout\"B,Z*github.com/functionx/fx-core/x/erc20/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'fx.erc20.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:fx.erc20.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'fx.erc20.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:fx.erc20.v1.Params)
  })
_sym_db.RegisterMessage(Params)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*github.com/functionx/fx-core/x/erc20/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['token_pairs']._options = None
  _GENESISSTATE.fields_by_name['token_pairs']._serialized_options = b'\310\336\037\000'
  _PARAMS.fields_by_name['enable_erc20']._options = None
  _PARAMS.fields_by_name['enable_erc20']._serialized_options = b'\362\336\037\023yaml:\"enable_erc20\"'
  _PARAMS.fields_by_name['enable_evm_hook']._options = None
  _PARAMS.fields_by_name['enable_evm_hook']._serialized_options = b'\342\336\037\rEnableEVMHook\362\336\037\026yaml:\"enable_evm_hook\"'
  _PARAMS.fields_by_name['ibc_timeout']._options = None
  _PARAMS.fields_by_name['ibc_timeout']._serialized_options = b'\230\337\037\001\310\336\037\000\362\336\037\022yaml:\"ibc_timeout\"'
  _GENESISSTATE._serialized_start=153
  _GENESISSTATE._serialized_end=261
  _PARAMS._serialized_start=264
  _PARAMS._serialized_end=469
# @@protoc_insertion_point(module_scope)
