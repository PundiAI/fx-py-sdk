# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/staking/v1beta1/staking.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from x.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from x.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from x.tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/staking/v1beta1/staking.proto\x12\x16\x63osmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1ctendermint/types/types.proto\"y\n\x0eHistoricalInfo\x12.\n\x06header\x18\x01 \x01(\x0b\x32\x18.tendermint.types.HeaderB\x04\xc8\xde\x1f\x00\x12\x37\n\x06valset\x18\x02 \x03(\x0b\x32!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00\"\x91\x02\n\x0f\x43ommissionRates\x12<\n\x04rate\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12S\n\x08max_rate\x18\x02 \x01(\tBA\xf2\xde\x1f\x0fyaml:\"max_rate\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x61\n\x0fmax_change_rate\x18\x03 \x01(\tBH\xf2\xde\x1f\x16yaml:\"max_change_rate\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00\"\xb4\x01\n\nCommission\x12K\n\x10\x63ommission_rates\x18\x01 \x01(\x0b\x32\'.cosmos.staking.v1beta1.CommissionRatesB\x08\xd0\xde\x1f\x01\xc8\xde\x1f\x00\x12O\n\x0bupdate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x1e\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x12yaml:\"update_time\":\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00\"\x93\x01\n\x0b\x44\x65scription\x12\x0f\n\x07moniker\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\x12\x0f\n\x07website\x18\x03 \x01(\t\x12\x35\n\x10security_contact\x18\x04 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:\"security_contact\"\x12\x0f\n\x07\x64\x65tails\x18\x05 \x01(\t:\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00\"\x95\x06\n\tValidator\x12\x35\n\x10operator_address\x18\x01 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:\"operator_address\"\x12\x63\n\x10\x63onsensus_pubkey\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB3\xca\xb4-\x14\x63osmos.crypto.PubKey\xf2\xde\x1f\x17yaml:\"consensus_pubkey\"\x12\x0e\n\x06jailed\x18\x03 \x01(\x08\x12\x32\n\x06status\x18\x04 \x01(\x0e\x32\".cosmos.staking.v1beta1.BondStatus\x12>\n\x06tokens\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x63\n\x10\x64\x65legator_shares\x18\x06 \x01(\tBI\xf2\xde\x1f\x17yaml:\"delegator_shares\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12>\n\x0b\x64\x65scription\x18\x07 \x01(\x0b\x32#.cosmos.staking.v1beta1.DescriptionB\x04\xc8\xde\x1f\x00\x12\x35\n\x10unbonding_height\x18\x08 \x01(\x03\x42\x1b\xf2\xde\x1f\x17yaml:\"unbonding_height\"\x12U\n\x0eunbonding_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB!\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x15yaml:\"unbonding_time\"\x12<\n\ncommission\x18\n \x01(\x0b\x32\".cosmos.staking.v1beta1.CommissionB\x04\xc8\xde\x1f\x00\x12i\n\x13min_self_delegation\x18\x0b \x01(\tBL\xf2\xde\x1f\x1ayaml:\"min_self_delegation\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00:\x0c\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\x88\xa0\x1f\x00\"+\n\x0cValAddresses\x12\x11\n\taddresses\x18\x01 \x03(\t:\x08\x98\xa0\x1f\x00\x80\xdc \x01\"\x88\x01\n\x06\x44VPair\x12\x37\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"delegator_address\"\x12\x37\n\x11validator_address\x18\x02 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"validator_address\":\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\">\n\x07\x44VPairs\x12\x33\n\x05pairs\x18\x01 \x03(\x0b\x32\x1e.cosmos.staking.v1beta1.DVPairB\x04\xc8\xde\x1f\x00\"\xd5\x01\n\nDVVTriplet\x12\x37\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"delegator_address\"\x12?\n\x15validator_src_address\x18\x02 \x01(\tB \xf2\xde\x1f\x1cyaml:\"validator_src_address\"\x12?\n\x15validator_dst_address\x18\x03 \x01(\tB \xf2\xde\x1f\x1cyaml:\"validator_dst_address\":\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"I\n\x0b\x44VVTriplets\x12:\n\x08triplets\x18\x01 \x03(\x0b\x32\".cosmos.staking.v1beta1.DVVTripletB\x04\xc8\xde\x1f\x00\"\xcc\x01\n\nDelegation\x12\x37\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"delegator_address\"\x12\x37\n\x11validator_address\x18\x02 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"validator_address\"\x12>\n\x06shares\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"\xde\x01\n\x13UnbondingDelegation\x12\x37\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"delegator_address\"\x12\x37\n\x11validator_address\x18\x02 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"validator_address\"\x12G\n\x07\x65ntries\x18\x03 \x03(\x0b\x32\x30.cosmos.staking.v1beta1.UnbondingDelegationEntryB\x04\xc8\xde\x1f\x00:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"\xd6\x02\n\x18UnbondingDelegationEntry\x12\x33\n\x0f\x63reation_height\x18\x01 \x01(\x03\x42\x1a\xf2\xde\x1f\x16yaml:\"creation_height\"\x12W\n\x0f\x63ompletion_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\"\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x16yaml:\"completion_time\"\x12\x61\n\x0finitial_balance\x18\x03 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:\"initial_balance\"\x12?\n\x07\x62\x61lance\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00\"\xd2\x02\n\x11RedelegationEntry\x12\x33\n\x0f\x63reation_height\x18\x01 \x01(\x03\x42\x1a\xf2\xde\x1f\x16yaml:\"creation_height\"\x12W\n\x0f\x63ompletion_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\"\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xf2\xde\x1f\x16yaml:\"completion_time\"\x12\x61\n\x0finitial_balance\x18\x03 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:\"initial_balance\"\x12\x42\n\nshares_dst\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00\"\x99\x02\n\x0cRedelegation\x12\x37\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:\"delegator_address\"\x12?\n\x15validator_src_address\x18\x02 \x01(\tB \xf2\xde\x1f\x1cyaml:\"validator_src_address\"\x12?\n\x15validator_dst_address\x18\x03 \x01(\tB \xf2\xde\x1f\x1cyaml:\"validator_dst_address\"\x12@\n\x07\x65ntries\x18\x04 \x03(\x0b\x32).cosmos.staking.v1beta1.RedelegationEntryB\x04\xc8\xde\x1f\x00:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"\xae\x02\n\x06Params\x12T\n\x0eunbonding_time\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB!\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x15yaml:\"unbonding_time\"\x12\x31\n\x0emax_validators\x18\x02 \x01(\rB\x19\xf2\xde\x1f\x15yaml:\"max_validators\"\x12+\n\x0bmax_entries\x18\x03 \x01(\rB\x16\xf2\xde\x1f\x12yaml:\"max_entries\"\x12\x39\n\x12historical_entries\x18\x04 \x01(\rB\x1d\xf2\xde\x1f\x19yaml:\"historical_entries\"\x12)\n\nbond_denom\x18\x05 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"bond_denom\":\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00\"\x8e\x01\n\x12\x44\x65legationResponse\x12<\n\ndelegation\x18\x01 \x01(\x0b\x32\".cosmos.staking.v1beta1.DelegationB\x04\xc8\xde\x1f\x00\x12\x30\n\x07\x62\x61lance\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x98\xa0\x1f\x00\"\xaf\x01\n\x19RedelegationEntryResponse\x12K\n\x12redelegation_entry\x18\x01 \x01(\x0b\x32).cosmos.staking.v1beta1.RedelegationEntryB\x04\xc8\xde\x1f\x00\x12?\n\x07\x62\x61lance\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01\"\xa8\x01\n\x14RedelegationResponse\x12@\n\x0credelegation\x18\x01 \x01(\x0b\x32$.cosmos.staking.v1beta1.RedelegationB\x04\xc8\xde\x1f\x00\x12H\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x31.cosmos.staking.v1beta1.RedelegationEntryResponseB\x04\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x00\"\xe0\x01\n\x04Pool\x12^\n\x11not_bonded_tokens\x18\x01 \x01(\tBC\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xea\xde\x1f\x11not_bonded_tokens\xc8\xde\x1f\x00\x12n\n\rbonded_tokens\x18\x02 \x01(\tBW\xea\xde\x1f\rbonded_tokens\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:\"bonded_tokens\":\x08\xf0\xa0\x1f\x01\xe8\xa0\x1f\x01*\xb6\x01\n\nBondStatus\x12,\n\x17\x42OND_STATUS_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bUnspecified\x12&\n\x14\x42OND_STATUS_UNBONDED\x10\x01\x1a\x0c\x8a\x9d \x08Unbonded\x12(\n\x15\x42OND_STATUS_UNBONDING\x10\x02\x1a\r\x8a\x9d \tUnbonding\x12\"\n\x12\x42OND_STATUS_BONDED\x10\x03\x1a\n\x8a\x9d \x06\x42onded\x1a\x04\x88\xa3\x1e\x00\x42.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')

_BONDSTATUS = DESCRIPTOR.enum_types_by_name['BondStatus']
BondStatus = enum_type_wrapper.EnumTypeWrapper(_BONDSTATUS)
BOND_STATUS_UNSPECIFIED = 0
BOND_STATUS_UNBONDED = 1
BOND_STATUS_UNBONDING = 2
BOND_STATUS_BONDED = 3


_HISTORICALINFO = DESCRIPTOR.message_types_by_name['HistoricalInfo']
_COMMISSIONRATES = DESCRIPTOR.message_types_by_name['CommissionRates']
_COMMISSION = DESCRIPTOR.message_types_by_name['Commission']
_DESCRIPTION = DESCRIPTOR.message_types_by_name['Description']
_VALIDATOR = DESCRIPTOR.message_types_by_name['Validator']
_VALADDRESSES = DESCRIPTOR.message_types_by_name['ValAddresses']
_DVPAIR = DESCRIPTOR.message_types_by_name['DVPair']
_DVPAIRS = DESCRIPTOR.message_types_by_name['DVPairs']
_DVVTRIPLET = DESCRIPTOR.message_types_by_name['DVVTriplet']
_DVVTRIPLETS = DESCRIPTOR.message_types_by_name['DVVTriplets']
_DELEGATION = DESCRIPTOR.message_types_by_name['Delegation']
_UNBONDINGDELEGATION = DESCRIPTOR.message_types_by_name['UnbondingDelegation']
_UNBONDINGDELEGATIONENTRY = DESCRIPTOR.message_types_by_name['UnbondingDelegationEntry']
_REDELEGATIONENTRY = DESCRIPTOR.message_types_by_name['RedelegationEntry']
_REDELEGATION = DESCRIPTOR.message_types_by_name['Redelegation']
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
_DELEGATIONRESPONSE = DESCRIPTOR.message_types_by_name['DelegationResponse']
_REDELEGATIONENTRYRESPONSE = DESCRIPTOR.message_types_by_name['RedelegationEntryResponse']
_REDELEGATIONRESPONSE = DESCRIPTOR.message_types_by_name['RedelegationResponse']
_POOL = DESCRIPTOR.message_types_by_name['Pool']
HistoricalInfo = _reflection.GeneratedProtocolMessageType('HistoricalInfo', (_message.Message,), {
  'DESCRIPTOR' : _HISTORICALINFO,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.HistoricalInfo)
  })
_sym_db.RegisterMessage(HistoricalInfo)

CommissionRates = _reflection.GeneratedProtocolMessageType('CommissionRates', (_message.Message,), {
  'DESCRIPTOR' : _COMMISSIONRATES,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.CommissionRates)
  })
_sym_db.RegisterMessage(CommissionRates)

Commission = _reflection.GeneratedProtocolMessageType('Commission', (_message.Message,), {
  'DESCRIPTOR' : _COMMISSION,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.Commission)
  })
_sym_db.RegisterMessage(Commission)

Description = _reflection.GeneratedProtocolMessageType('Description', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIPTION,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.Description)
  })
_sym_db.RegisterMessage(Description)

Validator = _reflection.GeneratedProtocolMessageType('Validator', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATOR,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.Validator)
  })
_sym_db.RegisterMessage(Validator)

ValAddresses = _reflection.GeneratedProtocolMessageType('ValAddresses', (_message.Message,), {
  'DESCRIPTOR' : _VALADDRESSES,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.ValAddresses)
  })
_sym_db.RegisterMessage(ValAddresses)

DVPair = _reflection.GeneratedProtocolMessageType('DVPair', (_message.Message,), {
  'DESCRIPTOR' : _DVPAIR,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.DVPair)
  })
_sym_db.RegisterMessage(DVPair)

DVPairs = _reflection.GeneratedProtocolMessageType('DVPairs', (_message.Message,), {
  'DESCRIPTOR' : _DVPAIRS,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.DVPairs)
  })
_sym_db.RegisterMessage(DVPairs)

DVVTriplet = _reflection.GeneratedProtocolMessageType('DVVTriplet', (_message.Message,), {
  'DESCRIPTOR' : _DVVTRIPLET,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.DVVTriplet)
  })
_sym_db.RegisterMessage(DVVTriplet)

DVVTriplets = _reflection.GeneratedProtocolMessageType('DVVTriplets', (_message.Message,), {
  'DESCRIPTOR' : _DVVTRIPLETS,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.DVVTriplets)
  })
_sym_db.RegisterMessage(DVVTriplets)

Delegation = _reflection.GeneratedProtocolMessageType('Delegation', (_message.Message,), {
  'DESCRIPTOR' : _DELEGATION,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.Delegation)
  })
_sym_db.RegisterMessage(Delegation)

UnbondingDelegation = _reflection.GeneratedProtocolMessageType('UnbondingDelegation', (_message.Message,), {
  'DESCRIPTOR' : _UNBONDINGDELEGATION,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.UnbondingDelegation)
  })
_sym_db.RegisterMessage(UnbondingDelegation)

UnbondingDelegationEntry = _reflection.GeneratedProtocolMessageType('UnbondingDelegationEntry', (_message.Message,), {
  'DESCRIPTOR' : _UNBONDINGDELEGATIONENTRY,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.UnbondingDelegationEntry)
  })
_sym_db.RegisterMessage(UnbondingDelegationEntry)

RedelegationEntry = _reflection.GeneratedProtocolMessageType('RedelegationEntry', (_message.Message,), {
  'DESCRIPTOR' : _REDELEGATIONENTRY,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.RedelegationEntry)
  })
_sym_db.RegisterMessage(RedelegationEntry)

Redelegation = _reflection.GeneratedProtocolMessageType('Redelegation', (_message.Message,), {
  'DESCRIPTOR' : _REDELEGATION,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.Redelegation)
  })
_sym_db.RegisterMessage(Redelegation)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.Params)
  })
_sym_db.RegisterMessage(Params)

DelegationResponse = _reflection.GeneratedProtocolMessageType('DelegationResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELEGATIONRESPONSE,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.DelegationResponse)
  })
_sym_db.RegisterMessage(DelegationResponse)

RedelegationEntryResponse = _reflection.GeneratedProtocolMessageType('RedelegationEntryResponse', (_message.Message,), {
  'DESCRIPTOR' : _REDELEGATIONENTRYRESPONSE,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.RedelegationEntryResponse)
  })
_sym_db.RegisterMessage(RedelegationEntryResponse)

RedelegationResponse = _reflection.GeneratedProtocolMessageType('RedelegationResponse', (_message.Message,), {
  'DESCRIPTOR' : _REDELEGATIONRESPONSE,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.RedelegationResponse)
  })
_sym_db.RegisterMessage(RedelegationResponse)

Pool = _reflection.GeneratedProtocolMessageType('Pool', (_message.Message,), {
  'DESCRIPTOR' : _POOL,
  '__module__' : 'cosmos.staking.v1beta1.staking_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.staking.v1beta1.Pool)
  })
_sym_db.RegisterMessage(Pool)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
  _BONDSTATUS._options = None
  _BONDSTATUS._serialized_options = b'\210\243\036\000'
  _BONDSTATUS.values_by_name["BOND_STATUS_UNSPECIFIED"]._options = None
  _BONDSTATUS.values_by_name["BOND_STATUS_UNSPECIFIED"]._serialized_options = b'\212\235 \013Unspecified'
  _BONDSTATUS.values_by_name["BOND_STATUS_UNBONDED"]._options = None
  _BONDSTATUS.values_by_name["BOND_STATUS_UNBONDED"]._serialized_options = b'\212\235 \010Unbonded'
  _BONDSTATUS.values_by_name["BOND_STATUS_UNBONDING"]._options = None
  _BONDSTATUS.values_by_name["BOND_STATUS_UNBONDING"]._serialized_options = b'\212\235 \tUnbonding'
  _BONDSTATUS.values_by_name["BOND_STATUS_BONDED"]._options = None
  _BONDSTATUS.values_by_name["BOND_STATUS_BONDED"]._serialized_options = b'\212\235 \006Bonded'
  _HISTORICALINFO.fields_by_name['header']._options = None
  _HISTORICALINFO.fields_by_name['header']._serialized_options = b'\310\336\037\000'
  _HISTORICALINFO.fields_by_name['valset']._options = None
  _HISTORICALINFO.fields_by_name['valset']._serialized_options = b'\310\336\037\000'
  _COMMISSIONRATES.fields_by_name['rate']._options = None
  _COMMISSIONRATES.fields_by_name['rate']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _COMMISSIONRATES.fields_by_name['max_rate']._options = None
  _COMMISSIONRATES.fields_by_name['max_rate']._serialized_options = b'\362\336\037\017yaml:\"max_rate\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _COMMISSIONRATES.fields_by_name['max_change_rate']._options = None
  _COMMISSIONRATES.fields_by_name['max_change_rate']._serialized_options = b'\362\336\037\026yaml:\"max_change_rate\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _COMMISSIONRATES._options = None
  _COMMISSIONRATES._serialized_options = b'\350\240\037\001\230\240\037\000'
  _COMMISSION.fields_by_name['commission_rates']._options = None
  _COMMISSION.fields_by_name['commission_rates']._serialized_options = b'\320\336\037\001\310\336\037\000'
  _COMMISSION.fields_by_name['update_time']._options = None
  _COMMISSION.fields_by_name['update_time']._serialized_options = b'\310\336\037\000\220\337\037\001\362\336\037\022yaml:\"update_time\"'
  _COMMISSION._options = None
  _COMMISSION._serialized_options = b'\350\240\037\001\230\240\037\000'
  _DESCRIPTION.fields_by_name['security_contact']._options = None
  _DESCRIPTION.fields_by_name['security_contact']._serialized_options = b'\362\336\037\027yaml:\"security_contact\"'
  _DESCRIPTION._options = None
  _DESCRIPTION._serialized_options = b'\350\240\037\001\230\240\037\000'
  _VALIDATOR.fields_by_name['operator_address']._options = None
  _VALIDATOR.fields_by_name['operator_address']._serialized_options = b'\362\336\037\027yaml:\"operator_address\"'
  _VALIDATOR.fields_by_name['consensus_pubkey']._options = None
  _VALIDATOR.fields_by_name['consensus_pubkey']._serialized_options = b'\312\264-\024cosmos.crypto.PubKey\362\336\037\027yaml:\"consensus_pubkey\"'
  _VALIDATOR.fields_by_name['tokens']._options = None
  _VALIDATOR.fields_by_name['tokens']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _VALIDATOR.fields_by_name['delegator_shares']._options = None
  _VALIDATOR.fields_by_name['delegator_shares']._serialized_options = b'\362\336\037\027yaml:\"delegator_shares\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _VALIDATOR.fields_by_name['description']._options = None
  _VALIDATOR.fields_by_name['description']._serialized_options = b'\310\336\037\000'
  _VALIDATOR.fields_by_name['unbonding_height']._options = None
  _VALIDATOR.fields_by_name['unbonding_height']._serialized_options = b'\362\336\037\027yaml:\"unbonding_height\"'
  _VALIDATOR.fields_by_name['unbonding_time']._options = None
  _VALIDATOR.fields_by_name['unbonding_time']._serialized_options = b'\310\336\037\000\220\337\037\001\362\336\037\025yaml:\"unbonding_time\"'
  _VALIDATOR.fields_by_name['commission']._options = None
  _VALIDATOR.fields_by_name['commission']._serialized_options = b'\310\336\037\000'
  _VALIDATOR.fields_by_name['min_self_delegation']._options = None
  _VALIDATOR.fields_by_name['min_self_delegation']._serialized_options = b'\362\336\037\032yaml:\"min_self_delegation\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _VALIDATOR._options = None
  _VALIDATOR._serialized_options = b'\350\240\037\000\230\240\037\000\210\240\037\000'
  _VALADDRESSES._options = None
  _VALADDRESSES._serialized_options = b'\230\240\037\000\200\334 \001'
  _DVPAIR.fields_by_name['delegator_address']._options = None
  _DVPAIR.fields_by_name['delegator_address']._serialized_options = b'\362\336\037\030yaml:\"delegator_address\"'
  _DVPAIR.fields_by_name['validator_address']._options = None
  _DVPAIR.fields_by_name['validator_address']._serialized_options = b'\362\336\037\030yaml:\"validator_address\"'
  _DVPAIR._options = None
  _DVPAIR._serialized_options = b'\350\240\037\000\210\240\037\000\230\240\037\000'
  _DVPAIRS.fields_by_name['pairs']._options = None
  _DVPAIRS.fields_by_name['pairs']._serialized_options = b'\310\336\037\000'
  _DVVTRIPLET.fields_by_name['delegator_address']._options = None
  _DVVTRIPLET.fields_by_name['delegator_address']._serialized_options = b'\362\336\037\030yaml:\"delegator_address\"'
  _DVVTRIPLET.fields_by_name['validator_src_address']._options = None
  _DVVTRIPLET.fields_by_name['validator_src_address']._serialized_options = b'\362\336\037\034yaml:\"validator_src_address\"'
  _DVVTRIPLET.fields_by_name['validator_dst_address']._options = None
  _DVVTRIPLET.fields_by_name['validator_dst_address']._serialized_options = b'\362\336\037\034yaml:\"validator_dst_address\"'
  _DVVTRIPLET._options = None
  _DVVTRIPLET._serialized_options = b'\350\240\037\000\210\240\037\000\230\240\037\000'
  _DVVTRIPLETS.fields_by_name['triplets']._options = None
  _DVVTRIPLETS.fields_by_name['triplets']._serialized_options = b'\310\336\037\000'
  _DELEGATION.fields_by_name['delegator_address']._options = None
  _DELEGATION.fields_by_name['delegator_address']._serialized_options = b'\362\336\037\030yaml:\"delegator_address\"'
  _DELEGATION.fields_by_name['validator_address']._options = None
  _DELEGATION.fields_by_name['validator_address']._serialized_options = b'\362\336\037\030yaml:\"validator_address\"'
  _DELEGATION.fields_by_name['shares']._options = None
  _DELEGATION.fields_by_name['shares']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _DELEGATION._options = None
  _DELEGATION._serialized_options = b'\350\240\037\000\210\240\037\000\230\240\037\000'
  _UNBONDINGDELEGATION.fields_by_name['delegator_address']._options = None
  _UNBONDINGDELEGATION.fields_by_name['delegator_address']._serialized_options = b'\362\336\037\030yaml:\"delegator_address\"'
  _UNBONDINGDELEGATION.fields_by_name['validator_address']._options = None
  _UNBONDINGDELEGATION.fields_by_name['validator_address']._serialized_options = b'\362\336\037\030yaml:\"validator_address\"'
  _UNBONDINGDELEGATION.fields_by_name['entries']._options = None
  _UNBONDINGDELEGATION.fields_by_name['entries']._serialized_options = b'\310\336\037\000'
  _UNBONDINGDELEGATION._options = None
  _UNBONDINGDELEGATION._serialized_options = b'\350\240\037\000\210\240\037\000\230\240\037\000'
  _UNBONDINGDELEGATIONENTRY.fields_by_name['creation_height']._options = None
  _UNBONDINGDELEGATIONENTRY.fields_by_name['creation_height']._serialized_options = b'\362\336\037\026yaml:\"creation_height\"'
  _UNBONDINGDELEGATIONENTRY.fields_by_name['completion_time']._options = None
  _UNBONDINGDELEGATIONENTRY.fields_by_name['completion_time']._serialized_options = b'\310\336\037\000\220\337\037\001\362\336\037\026yaml:\"completion_time\"'
  _UNBONDINGDELEGATIONENTRY.fields_by_name['initial_balance']._options = None
  _UNBONDINGDELEGATIONENTRY.fields_by_name['initial_balance']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000\362\336\037\026yaml:\"initial_balance\"'
  _UNBONDINGDELEGATIONENTRY.fields_by_name['balance']._options = None
  _UNBONDINGDELEGATIONENTRY.fields_by_name['balance']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _UNBONDINGDELEGATIONENTRY._options = None
  _UNBONDINGDELEGATIONENTRY._serialized_options = b'\350\240\037\001\230\240\037\000'
  _REDELEGATIONENTRY.fields_by_name['creation_height']._options = None
  _REDELEGATIONENTRY.fields_by_name['creation_height']._serialized_options = b'\362\336\037\026yaml:\"creation_height\"'
  _REDELEGATIONENTRY.fields_by_name['completion_time']._options = None
  _REDELEGATIONENTRY.fields_by_name['completion_time']._serialized_options = b'\310\336\037\000\220\337\037\001\362\336\037\026yaml:\"completion_time\"'
  _REDELEGATIONENTRY.fields_by_name['initial_balance']._options = None
  _REDELEGATIONENTRY.fields_by_name['initial_balance']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000\362\336\037\026yaml:\"initial_balance\"'
  _REDELEGATIONENTRY.fields_by_name['shares_dst']._options = None
  _REDELEGATIONENTRY.fields_by_name['shares_dst']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _REDELEGATIONENTRY._options = None
  _REDELEGATIONENTRY._serialized_options = b'\350\240\037\001\230\240\037\000'
  _REDELEGATION.fields_by_name['delegator_address']._options = None
  _REDELEGATION.fields_by_name['delegator_address']._serialized_options = b'\362\336\037\030yaml:\"delegator_address\"'
  _REDELEGATION.fields_by_name['validator_src_address']._options = None
  _REDELEGATION.fields_by_name['validator_src_address']._serialized_options = b'\362\336\037\034yaml:\"validator_src_address\"'
  _REDELEGATION.fields_by_name['validator_dst_address']._options = None
  _REDELEGATION.fields_by_name['validator_dst_address']._serialized_options = b'\362\336\037\034yaml:\"validator_dst_address\"'
  _REDELEGATION.fields_by_name['entries']._options = None
  _REDELEGATION.fields_by_name['entries']._serialized_options = b'\310\336\037\000'
  _REDELEGATION._options = None
  _REDELEGATION._serialized_options = b'\350\240\037\000\210\240\037\000\230\240\037\000'
  _PARAMS.fields_by_name['unbonding_time']._options = None
  _PARAMS.fields_by_name['unbonding_time']._serialized_options = b'\310\336\037\000\230\337\037\001\362\336\037\025yaml:\"unbonding_time\"'
  _PARAMS.fields_by_name['max_validators']._options = None
  _PARAMS.fields_by_name['max_validators']._serialized_options = b'\362\336\037\025yaml:\"max_validators\"'
  _PARAMS.fields_by_name['max_entries']._options = None
  _PARAMS.fields_by_name['max_entries']._serialized_options = b'\362\336\037\022yaml:\"max_entries\"'
  _PARAMS.fields_by_name['historical_entries']._options = None
  _PARAMS.fields_by_name['historical_entries']._serialized_options = b'\362\336\037\031yaml:\"historical_entries\"'
  _PARAMS.fields_by_name['bond_denom']._options = None
  _PARAMS.fields_by_name['bond_denom']._serialized_options = b'\362\336\037\021yaml:\"bond_denom\"'
  _PARAMS._options = None
  _PARAMS._serialized_options = b'\350\240\037\001\230\240\037\000'
  _DELEGATIONRESPONSE.fields_by_name['delegation']._options = None
  _DELEGATIONRESPONSE.fields_by_name['delegation']._serialized_options = b'\310\336\037\000'
  _DELEGATIONRESPONSE.fields_by_name['balance']._options = None
  _DELEGATIONRESPONSE.fields_by_name['balance']._serialized_options = b'\310\336\037\000'
  _DELEGATIONRESPONSE._options = None
  _DELEGATIONRESPONSE._serialized_options = b'\350\240\037\000\230\240\037\000'
  _REDELEGATIONENTRYRESPONSE.fields_by_name['redelegation_entry']._options = None
  _REDELEGATIONENTRYRESPONSE.fields_by_name['redelegation_entry']._serialized_options = b'\310\336\037\000'
  _REDELEGATIONENTRYRESPONSE.fields_by_name['balance']._options = None
  _REDELEGATIONENTRYRESPONSE.fields_by_name['balance']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _REDELEGATIONENTRYRESPONSE._options = None
  _REDELEGATIONENTRYRESPONSE._serialized_options = b'\350\240\037\001'
  _REDELEGATIONRESPONSE.fields_by_name['redelegation']._options = None
  _REDELEGATIONRESPONSE.fields_by_name['redelegation']._serialized_options = b'\310\336\037\000'
  _REDELEGATIONRESPONSE.fields_by_name['entries']._options = None
  _REDELEGATIONRESPONSE.fields_by_name['entries']._serialized_options = b'\310\336\037\000'
  _REDELEGATIONRESPONSE._options = None
  _REDELEGATIONRESPONSE._serialized_options = b'\350\240\037\000'
  _POOL.fields_by_name['not_bonded_tokens']._options = None
  _POOL.fields_by_name['not_bonded_tokens']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\352\336\037\021not_bonded_tokens\310\336\037\000'
  _POOL.fields_by_name['bonded_tokens']._options = None
  _POOL.fields_by_name['bonded_tokens']._serialized_options = b'\352\336\037\rbonded_tokens\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000\362\336\037\024yaml:\"bonded_tokens\"'
  _POOL._options = None
  _POOL._serialized_options = b'\360\240\037\001\350\240\037\001'
  _BONDSTATUS._serialized_start=4759
  _BONDSTATUS._serialized_end=4941
  _HISTORICALINFO._serialized_start=267
  _HISTORICALINFO._serialized_end=388
  _COMMISSIONRATES._serialized_start=391
  _COMMISSIONRATES._serialized_end=664
  _COMMISSION._serialized_start=667
  _COMMISSION._serialized_end=847
  _DESCRIPTION._serialized_start=850
  _DESCRIPTION._serialized_end=997
  _VALIDATOR._serialized_start=1000
  _VALIDATOR._serialized_end=1789
  _VALADDRESSES._serialized_start=1791
  _VALADDRESSES._serialized_end=1834
  _DVPAIR._serialized_start=1837
  _DVPAIR._serialized_end=1973
  _DVPAIRS._serialized_start=1975
  _DVPAIRS._serialized_end=2037
  _DVVTRIPLET._serialized_start=2040
  _DVVTRIPLET._serialized_end=2253
  _DVVTRIPLETS._serialized_start=2255
  _DVVTRIPLETS._serialized_end=2328
  _DELEGATION._serialized_start=2331
  _DELEGATION._serialized_end=2535
  _UNBONDINGDELEGATION._serialized_start=2538
  _UNBONDINGDELEGATION._serialized_end=2760
  _UNBONDINGDELEGATIONENTRY._serialized_start=2763
  _UNBONDINGDELEGATIONENTRY._serialized_end=3105
  _REDELEGATIONENTRY._serialized_start=3108
  _REDELEGATIONENTRY._serialized_end=3446
  _REDELEGATION._serialized_start=3449
  _REDELEGATION._serialized_end=3730
  _PARAMS._serialized_start=3733
  _PARAMS._serialized_end=4035
  _DELEGATIONRESPONSE._serialized_start=4038
  _DELEGATIONRESPONSE._serialized_end=4180
  _REDELEGATIONENTRYRESPONSE._serialized_start=4183
  _REDELEGATIONENTRYRESPONSE._serialized_end=4358
  _REDELEGATIONRESPONSE._serialized_start=4361
  _REDELEGATIONRESPONSE._serialized_end=4529
  _POOL._serialized_start=4532
  _POOL._serialized_end=4756
# @@protoc_insertion_point(module_scope)
