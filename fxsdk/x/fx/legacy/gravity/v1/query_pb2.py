# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/legacy/gravity/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxsdk.x.fx.legacy.gravity.v1 import genesis_pb2 as fx_dot_legacy_dot_gravity_dot_v1_dot_genesis__pb2
from fxsdk.x.fx.legacy.gravity.v1 import tx_pb2 as fx_dot_legacy_dot_gravity_dot_v1_dot_tx__pb2
from fxsdk.x.fx.legacy.gravity.v1 import types_pb2 as fx_dot_legacy_dot_gravity_dot_v1_dot_types__pb2
from fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n fx/legacy/gravity/v1/query.proto\x12\rfx.gravity.v1\x1a\"fx/legacy/gravity/v1/genesis.proto\x1a\x1d\x66x/legacy/gravity/v1/tx.proto\x1a fx/legacy/gravity/v1/types.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\"\x14\n\x12QueryParamsRequest\"B\n\x13QueryParamsResponse\x12+\n\x06params\x18\x01 \x01(\x0b\x32\x15.fx.gravity.v1.ParamsB\x04\xc8\xde\x1f\x00\"\x1b\n\x19QueryCurrentValsetRequest\"C\n\x1aQueryCurrentValsetResponse\x12%\n\x06valset\x18\x01 \x01(\x0b\x32\x15.fx.gravity.v1.Valset\"*\n\x19QueryValsetRequestRequest\x12\r\n\x05nonce\x18\x01 \x01(\x04\"C\n\x1aQueryValsetRequestResponse\x12%\n\x06valset\x18\x01 \x01(\x0b\x32\x15.fx.gravity.v1.Valset\";\n\x19QueryValsetConfirmRequest\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"N\n\x1aQueryValsetConfirmResponse\x12\x30\n\x07\x63onfirm\x18\x01 \x01(\x0b\x32\x1f.fx.gravity.v1.MsgValsetConfirm\"2\n!QueryValsetConfirmsByNonceRequest\x12\r\n\x05nonce\x18\x01 \x01(\x04\"W\n\"QueryValsetConfirmsByNonceResponse\x12\x31\n\x08\x63onfirms\x18\x01 \x03(\x0b\x32\x1f.fx.gravity.v1.MsgValsetConfirm\" \n\x1eQueryLastValsetRequestsRequest\"I\n\x1fQueryLastValsetRequestsResponse\x12&\n\x07valsets\x18\x01 \x03(\x0b\x32\x15.fx.gravity.v1.Valset\"=\n*QueryLastPendingValsetRequestByAddrRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"U\n+QueryLastPendingValsetRequestByAddrResponse\x12&\n\x07valsets\x18\x01 \x03(\x0b\x32\x15.fx.gravity.v1.Valset\"N\n\x14QueryBatchFeeRequest\x12\x36\n\x0cminBatchFees\x18\x01 \x03(\x0b\x32\x1a.fx.gravity.v1.MinBatchFeeB\x04\xc8\xde\x1f\x00\"E\n\x15QueryBatchFeeResponse\x12,\n\nbatch_fees\x18\x01 \x03(\x0b\x32\x18.fx.gravity.v1.BatchFees\"<\n)QueryLastPendingBatchRequestByAddrRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"[\n*QueryLastPendingBatchRequestByAddrResponse\x12-\n\x05\x62\x61tch\x18\x01 \x01(\x0b\x32\x1e.fx.gravity.v1.OutgoingTxBatch\"\x1f\n\x1dQueryOutgoingTxBatchesRequest\"Q\n\x1eQueryOutgoingTxBatchesResponse\x12/\n\x07\x62\x61tches\x18\x01 \x03(\x0b\x32\x1e.fx.gravity.v1.OutgoingTxBatch\"H\n\x1fQueryBatchRequestByNonceRequest\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x02 \x01(\t\"Q\n QueryBatchRequestByNonceResponse\x12-\n\x05\x62\x61tch\x18\x01 \x01(\x0b\x32\x1e.fx.gravity.v1.OutgoingTxBatch\"R\n\x18QueryBatchConfirmRequest\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\"L\n\x19QueryBatchConfirmResponse\x12/\n\x07\x63onfirm\x18\x01 \x01(\x0b\x32\x1e.fx.gravity.v1.MsgConfirmBatch\"B\n\x19QueryBatchConfirmsRequest\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x02 \x01(\t\"N\n\x1aQueryBatchConfirmsResponse\x12\x30\n\x08\x63onfirms\x18\x01 \x03(\x0b\x32\x1e.fx.gravity.v1.MsgConfirmBatch\"3\n QueryLastEventNonceByAddrRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"8\n!QueryLastEventNonceByAddrResponse\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\")\n\x18QueryERC20ToDenomRequest\x12\r\n\x05\x65rc20\x18\x01 \x01(\t\"A\n\x19QueryERC20ToDenomResponse\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x15\n\rfx_originated\x18\x02 \x01(\x08\")\n\x18QueryDenomToERC20Request\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\"A\n\x19QueryDenomToERC20Response\x12\r\n\x05\x65rc20\x18\x01 \x01(\t\x12\x15\n\rfx_originated\x18\x02 \x01(\x08\"?\n\"QueryDelegateKeyByValidatorRequest\x12\x19\n\x11validator_address\x18\x01 \x01(\t\"X\n#QueryDelegateKeyByValidatorResponse\x12\x13\n\x0b\x65th_address\x18\x01 \x01(\t\x12\x1c\n\x14orchestrator_address\x18\x02 \x01(\t\"3\n\x1cQueryDelegateKeyByEthRequest\x12\x13\n\x0b\x65th_address\x18\x01 \x01(\t\"X\n\x1dQueryDelegateKeyByEthResponse\x12\x19\n\x11validator_address\x18\x01 \x01(\t\x12\x1c\n\x14orchestrator_address\x18\x02 \x01(\t\"E\n%QueryDelegateKeyByOrchestratorRequest\x12\x1c\n\x14orchestrator_address\x18\x01 \x01(\t\"X\n&QueryDelegateKeyByOrchestratorResponse\x12\x19\n\x11validator_address\x18\x01 \x01(\t\x12\x13\n\x0b\x65th_address\x18\x02 \x01(\t\"6\n\x1cQueryPendingSendToEthRequest\x12\x16\n\x0esender_address\x18\x01 \x01(\t\"\xa0\x01\n\x1dQueryPendingSendToEthResponse\x12?\n\x14transfers_in_batches\x18\x01 \x03(\x0b\x32!.fx.gravity.v1.OutgoingTransferTx\x12>\n\x13unbatched_transfers\x18\x02 \x03(\x0b\x32!.fx.gravity.v1.OutgoingTransferTx\"%\n#QueryLastObservedBlockHeightRequest\"V\n$QueryLastObservedBlockHeightResponse\x12\x18\n\x10\x65th_block_height\x18\x01 \x01(\x04\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x04\"9\n&QueryLastEventBlockHeightByAddrRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"?\n\'QueryLastEventBlockHeightByAddrResponse\x12\x14\n\x0c\x62lock_height\x18\x01 \x01(\x04\")\n\'QueryProjectedBatchTimeoutHeightRequest\"B\n(QueryProjectedBatchTimeoutHeightResponse\x12\x16\n\x0etimeout_height\x18\x01 \x01(\x04\"\x1a\n\x18QueryBridgeTokensRequest\"O\n\x19QueryBridgeTokensResponse\x12\x32\n\rbridge_tokens\x18\x01 \x03(\x0b\x32\x1b.fx.gravity.v1.ERC20ToDenom2\xe0\x1d\n\x05Query\x12n\n\x06Params\x12!.fx.gravity.v1.QueryParamsRequest\x1a\".fx.gravity.v1.QueryParamsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/fx/gravity/v1/params\x12\x8b\x01\n\rCurrentValset\x12(.fx.gravity.v1.QueryCurrentValsetRequest\x1a).fx.gravity.v1.QueryCurrentValsetResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/fx/gravity/v1/valset/current\x12\x8b\x01\n\rValsetRequest\x12(.fx.gravity.v1.QueryValsetRequestRequest\x1a).fx.gravity.v1.QueryValsetRequestResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/fx/gravity/v1/valset/request\x12\x8b\x01\n\rValsetConfirm\x12(.fx.gravity.v1.QueryValsetConfirmRequest\x1a).fx.gravity.v1.QueryValsetConfirmResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/fx/gravity/v1/valset/confirm\x12\xa4\x01\n\x15ValsetConfirmsByNonce\x12\x30.fx.gravity.v1.QueryValsetConfirmsByNonceRequest\x1a\x31.fx.gravity.v1.QueryValsetConfirmsByNonceResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/fx/gravity/v1/valset/confirms\x12\x9b\x01\n\x12LastValsetRequests\x12-.fx.gravity.v1.QueryLastValsetRequestsRequest\x1a..fx.gravity.v1.QueryLastValsetRequestsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/fx/gravity/v1/valset/requests\x12\xbb\x01\n\x1eLastPendingValsetRequestByAddr\x12\x39.fx.gravity.v1.QueryLastPendingValsetRequestByAddrRequest\x1a:.fx.gravity.v1.QueryLastPendingValsetRequestByAddrResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/fx/gravity/v1/valset/last\x12\xb7\x01\n\x1dLastPendingBatchRequestByAddr\x12\x38.fx.gravity.v1.QueryLastPendingBatchRequestByAddrRequest\x1a\x39.fx.gravity.v1.QueryLastPendingBatchRequestByAddrResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/fx/gravity/v1/batch/last\x12\xae\x01\n\x14LastEventNonceByAddr\x12/.fx.gravity.v1.QueryLastEventNonceByAddrRequest\x1a\x30.fx.gravity.v1.QueryLastEventNonceByAddrResponse\"3\x82\xd3\xe4\x93\x02-\x12+/fx/gravity/v1/oracle/event_nonce/{address}\x12\xc7\x01\n\x1aLastEventBlockHeightByAddr\x12\x35.fx.gravity.v1.QueryLastEventBlockHeightByAddrRequest\x1a\x36.fx.gravity.v1.QueryLastEventBlockHeightByAddrResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/fx/gravity/v1/oracle/event/block_height/{address}\x12y\n\tBatchFees\x12#.fx.gravity.v1.QueryBatchFeeRequest\x1a$.fx.gravity.v1.QueryBatchFeeResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/fx/gravity/v1/batch_fees\x12\xb0\x01\n\x17LastObservedBlockHeight\x12\x32.fx.gravity.v1.QueryLastObservedBlockHeightRequest\x1a\x33.fx.gravity.v1.QueryLastObservedBlockHeightResponse\",\x82\xd3\xe4\x93\x02&\x12$/fx/gravity/v1/observed/block_height\x12\x9a\x01\n\x11OutgoingTxBatches\x12,.fx.gravity.v1.QueryOutgoingTxBatchesRequest\x1a-.fx.gravity.v1.QueryOutgoingTxBatchesResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /fx/gravity/v1/batch/outgoing_tx\x12\x9c\x01\n\x13\x42\x61tchRequestByNonce\x12..fx.gravity.v1.QueryBatchRequestByNonceRequest\x1a/.fx.gravity.v1.QueryBatchRequestByNonceResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/fx/gravity/v1/batch/request\x12\x87\x01\n\x0c\x42\x61tchConfirm\x12\'.fx.gravity.v1.QueryBatchConfirmRequest\x1a(.fx.gravity.v1.QueryBatchConfirmResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/fx/gravity/v1/batch/confirm\x12\x8b\x01\n\rBatchConfirms\x12(.fx.gravity.v1.QueryBatchConfirmsRequest\x1a).fx.gravity.v1.QueryBatchConfirmsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/fx/gravity/v1/batch/confirms\x12\x7f\n\x0c\x45RC20ToDenom\x12\'.fx.gravity.v1.QueryERC20ToDenomRequest\x1a(.fx.gravity.v1.QueryERC20ToDenomResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/fx/gravity/v1/denom\x12\x7f\n\x0c\x44\x65nomToERC20\x12\'.fx.gravity.v1.QueryDenomToERC20Request\x1a(.fx.gravity.v1.QueryDenomToERC20Response\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/fx/gravity/v1/erc20\x12\xb4\x01\n\x19GetDelegateKeyByValidator\x12\x31.fx.gravity.v1.QueryDelegateKeyByValidatorRequest\x1a\x32.fx.gravity.v1.QueryDelegateKeyByValidatorResponse\"0\x82\xd3\xe4\x93\x02*\x12(/fx/gravity/v1/delegate_key_by_validator\x12\x9c\x01\n\x13GetDelegateKeyByEth\x12+.fx.gravity.v1.QueryDelegateKeyByEthRequest\x1a,.fx.gravity.v1.QueryDelegateKeyByEthResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/fx/gravity/v1/delegate_key_by_eth\x12\xc0\x01\n\x1cGetDelegateKeyByOrchestrator\x12\x34.fx.gravity.v1.QueryDelegateKeyByOrchestratorRequest\x1a\x35.fx.gravity.v1.QueryDelegateKeyByOrchestratorResponse\"3\x82\xd3\xe4\x93\x02-\x12+/fx/gravity/v1/delegate_key_by_orchestrator\x12\x9c\x01\n\x13GetPendingSendToEth\x12+.fx.gravity.v1.QueryPendingSendToEthRequest\x1a,.fx.gravity.v1.QueryPendingSendToEthResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/fx/gravity/v1/pending_send_to_eth\x12\xbe\x01\n\x1bProjectedBatchTimeoutHeight\x12\x36.fx.gravity.v1.QueryProjectedBatchTimeoutHeightRequest\x1a\x37.fx.gravity.v1.QueryProjectedBatchTimeoutHeightResponse\".\x82\xd3\xe4\x93\x02(\x12&/fx/gravity/v1/projected_batch_timeout\x12\x87\x01\n\x0c\x42ridgeTokens\x12\'.fx.gravity.v1.QueryBridgeTokensRequest\x1a(.fx.gravity.v1.QueryBridgeTokensResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/fx/gravity/v1/bridge_tokensB.Z,github.com/functionx/fx-core/x/gravity/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fx.legacy.gravity.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/functionx/fx-core/x/gravity/types'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERYBATCHFEEREQUEST.fields_by_name['minBatchFees']._options = None
  _QUERYBATCHFEEREQUEST.fields_by_name['minBatchFees']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\027\022\025/fx/gravity/v1/params'
  _QUERY.methods_by_name['CurrentValset']._options = None
  _QUERY.methods_by_name['CurrentValset']._serialized_options = b'\202\323\344\223\002\037\022\035/fx/gravity/v1/valset/current'
  _QUERY.methods_by_name['ValsetRequest']._options = None
  _QUERY.methods_by_name['ValsetRequest']._serialized_options = b'\202\323\344\223\002\037\022\035/fx/gravity/v1/valset/request'
  _QUERY.methods_by_name['ValsetConfirm']._options = None
  _QUERY.methods_by_name['ValsetConfirm']._serialized_options = b'\202\323\344\223\002\037\022\035/fx/gravity/v1/valset/confirm'
  _QUERY.methods_by_name['ValsetConfirmsByNonce']._options = None
  _QUERY.methods_by_name['ValsetConfirmsByNonce']._serialized_options = b'\202\323\344\223\002 \022\036/fx/gravity/v1/valset/confirms'
  _QUERY.methods_by_name['LastValsetRequests']._options = None
  _QUERY.methods_by_name['LastValsetRequests']._serialized_options = b'\202\323\344\223\002 \022\036/fx/gravity/v1/valset/requests'
  _QUERY.methods_by_name['LastPendingValsetRequestByAddr']._options = None
  _QUERY.methods_by_name['LastPendingValsetRequestByAddr']._serialized_options = b'\202\323\344\223\002\034\022\032/fx/gravity/v1/valset/last'
  _QUERY.methods_by_name['LastPendingBatchRequestByAddr']._options = None
  _QUERY.methods_by_name['LastPendingBatchRequestByAddr']._serialized_options = b'\202\323\344\223\002\033\022\031/fx/gravity/v1/batch/last'
  _QUERY.methods_by_name['LastEventNonceByAddr']._options = None
  _QUERY.methods_by_name['LastEventNonceByAddr']._serialized_options = b'\202\323\344\223\002-\022+/fx/gravity/v1/oracle/event_nonce/{address}'
  _QUERY.methods_by_name['LastEventBlockHeightByAddr']._options = None
  _QUERY.methods_by_name['LastEventBlockHeightByAddr']._serialized_options = b'\202\323\344\223\0024\0222/fx/gravity/v1/oracle/event/block_height/{address}'
  _QUERY.methods_by_name['BatchFees']._options = None
  _QUERY.methods_by_name['BatchFees']._serialized_options = b'\202\323\344\223\002\033\022\031/fx/gravity/v1/batch_fees'
  _QUERY.methods_by_name['LastObservedBlockHeight']._options = None
  _QUERY.methods_by_name['LastObservedBlockHeight']._serialized_options = b'\202\323\344\223\002&\022$/fx/gravity/v1/observed/block_height'
  _QUERY.methods_by_name['OutgoingTxBatches']._options = None
  _QUERY.methods_by_name['OutgoingTxBatches']._serialized_options = b'\202\323\344\223\002\"\022 /fx/gravity/v1/batch/outgoing_tx'
  _QUERY.methods_by_name['BatchRequestByNonce']._options = None
  _QUERY.methods_by_name['BatchRequestByNonce']._serialized_options = b'\202\323\344\223\002\036\022\034/fx/gravity/v1/batch/request'
  _QUERY.methods_by_name['BatchConfirm']._options = None
  _QUERY.methods_by_name['BatchConfirm']._serialized_options = b'\202\323\344\223\002\036\022\034/fx/gravity/v1/batch/confirm'
  _QUERY.methods_by_name['BatchConfirms']._options = None
  _QUERY.methods_by_name['BatchConfirms']._serialized_options = b'\202\323\344\223\002\037\022\035/fx/gravity/v1/batch/confirms'
  _QUERY.methods_by_name['ERC20ToDenom']._options = None
  _QUERY.methods_by_name['ERC20ToDenom']._serialized_options = b'\202\323\344\223\002\026\022\024/fx/gravity/v1/denom'
  _QUERY.methods_by_name['DenomToERC20']._options = None
  _QUERY.methods_by_name['DenomToERC20']._serialized_options = b'\202\323\344\223\002\026\022\024/fx/gravity/v1/erc20'
  _QUERY.methods_by_name['GetDelegateKeyByValidator']._options = None
  _QUERY.methods_by_name['GetDelegateKeyByValidator']._serialized_options = b'\202\323\344\223\002*\022(/fx/gravity/v1/delegate_key_by_validator'
  _QUERY.methods_by_name['GetDelegateKeyByEth']._options = None
  _QUERY.methods_by_name['GetDelegateKeyByEth']._serialized_options = b'\202\323\344\223\002$\022\"/fx/gravity/v1/delegate_key_by_eth'
  _QUERY.methods_by_name['GetDelegateKeyByOrchestrator']._options = None
  _QUERY.methods_by_name['GetDelegateKeyByOrchestrator']._serialized_options = b'\202\323\344\223\002-\022+/fx/gravity/v1/delegate_key_by_orchestrator'
  _QUERY.methods_by_name['GetPendingSendToEth']._options = None
  _QUERY.methods_by_name['GetPendingSendToEth']._serialized_options = b'\202\323\344\223\002$\022\"/fx/gravity/v1/pending_send_to_eth'
  _QUERY.methods_by_name['ProjectedBatchTimeoutHeight']._options = None
  _QUERY.methods_by_name['ProjectedBatchTimeoutHeight']._serialized_options = b'\202\323\344\223\002(\022&/fx/gravity/v1/projected_batch_timeout'
  _QUERY.methods_by_name['BridgeTokens']._options = None
  _QUERY.methods_by_name['BridgeTokens']._serialized_options = b'\202\323\344\223\002\036\022\034/fx/gravity/v1/bridge_tokens'
  _globals['_QUERYPARAMSREQUEST']._serialized_start=204
  _globals['_QUERYPARAMSREQUEST']._serialized_end=224
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=226
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=292
  _globals['_QUERYCURRENTVALSETREQUEST']._serialized_start=294
  _globals['_QUERYCURRENTVALSETREQUEST']._serialized_end=321
  _globals['_QUERYCURRENTVALSETRESPONSE']._serialized_start=323
  _globals['_QUERYCURRENTVALSETRESPONSE']._serialized_end=390
  _globals['_QUERYVALSETREQUESTREQUEST']._serialized_start=392
  _globals['_QUERYVALSETREQUESTREQUEST']._serialized_end=434
  _globals['_QUERYVALSETREQUESTRESPONSE']._serialized_start=436
  _globals['_QUERYVALSETREQUESTRESPONSE']._serialized_end=503
  _globals['_QUERYVALSETCONFIRMREQUEST']._serialized_start=505
  _globals['_QUERYVALSETCONFIRMREQUEST']._serialized_end=564
  _globals['_QUERYVALSETCONFIRMRESPONSE']._serialized_start=566
  _globals['_QUERYVALSETCONFIRMRESPONSE']._serialized_end=644
  _globals['_QUERYVALSETCONFIRMSBYNONCEREQUEST']._serialized_start=646
  _globals['_QUERYVALSETCONFIRMSBYNONCEREQUEST']._serialized_end=696
  _globals['_QUERYVALSETCONFIRMSBYNONCERESPONSE']._serialized_start=698
  _globals['_QUERYVALSETCONFIRMSBYNONCERESPONSE']._serialized_end=785
  _globals['_QUERYLASTVALSETREQUESTSREQUEST']._serialized_start=787
  _globals['_QUERYLASTVALSETREQUESTSREQUEST']._serialized_end=819
  _globals['_QUERYLASTVALSETREQUESTSRESPONSE']._serialized_start=821
  _globals['_QUERYLASTVALSETREQUESTSRESPONSE']._serialized_end=894
  _globals['_QUERYLASTPENDINGVALSETREQUESTBYADDRREQUEST']._serialized_start=896
  _globals['_QUERYLASTPENDINGVALSETREQUESTBYADDRREQUEST']._serialized_end=957
  _globals['_QUERYLASTPENDINGVALSETREQUESTBYADDRRESPONSE']._serialized_start=959
  _globals['_QUERYLASTPENDINGVALSETREQUESTBYADDRRESPONSE']._serialized_end=1044
  _globals['_QUERYBATCHFEEREQUEST']._serialized_start=1046
  _globals['_QUERYBATCHFEEREQUEST']._serialized_end=1124
  _globals['_QUERYBATCHFEERESPONSE']._serialized_start=1126
  _globals['_QUERYBATCHFEERESPONSE']._serialized_end=1195
  _globals['_QUERYLASTPENDINGBATCHREQUESTBYADDRREQUEST']._serialized_start=1197
  _globals['_QUERYLASTPENDINGBATCHREQUESTBYADDRREQUEST']._serialized_end=1257
  _globals['_QUERYLASTPENDINGBATCHREQUESTBYADDRRESPONSE']._serialized_start=1259
  _globals['_QUERYLASTPENDINGBATCHREQUESTBYADDRRESPONSE']._serialized_end=1350
  _globals['_QUERYOUTGOINGTXBATCHESREQUEST']._serialized_start=1352
  _globals['_QUERYOUTGOINGTXBATCHESREQUEST']._serialized_end=1383
  _globals['_QUERYOUTGOINGTXBATCHESRESPONSE']._serialized_start=1385
  _globals['_QUERYOUTGOINGTXBATCHESRESPONSE']._serialized_end=1466
  _globals['_QUERYBATCHREQUESTBYNONCEREQUEST']._serialized_start=1468
  _globals['_QUERYBATCHREQUESTBYNONCEREQUEST']._serialized_end=1540
  _globals['_QUERYBATCHREQUESTBYNONCERESPONSE']._serialized_start=1542
  _globals['_QUERYBATCHREQUESTBYNONCERESPONSE']._serialized_end=1623
  _globals['_QUERYBATCHCONFIRMREQUEST']._serialized_start=1625
  _globals['_QUERYBATCHCONFIRMREQUEST']._serialized_end=1707
  _globals['_QUERYBATCHCONFIRMRESPONSE']._serialized_start=1709
  _globals['_QUERYBATCHCONFIRMRESPONSE']._serialized_end=1785
  _globals['_QUERYBATCHCONFIRMSREQUEST']._serialized_start=1787
  _globals['_QUERYBATCHCONFIRMSREQUEST']._serialized_end=1853
  _globals['_QUERYBATCHCONFIRMSRESPONSE']._serialized_start=1855
  _globals['_QUERYBATCHCONFIRMSRESPONSE']._serialized_end=1933
  _globals['_QUERYLASTEVENTNONCEBYADDRREQUEST']._serialized_start=1935
  _globals['_QUERYLASTEVENTNONCEBYADDRREQUEST']._serialized_end=1986
  _globals['_QUERYLASTEVENTNONCEBYADDRRESPONSE']._serialized_start=1988
  _globals['_QUERYLASTEVENTNONCEBYADDRRESPONSE']._serialized_end=2044
  _globals['_QUERYERC20TODENOMREQUEST']._serialized_start=2046
  _globals['_QUERYERC20TODENOMREQUEST']._serialized_end=2087
  _globals['_QUERYERC20TODENOMRESPONSE']._serialized_start=2089
  _globals['_QUERYERC20TODENOMRESPONSE']._serialized_end=2154
  _globals['_QUERYDENOMTOERC20REQUEST']._serialized_start=2156
  _globals['_QUERYDENOMTOERC20REQUEST']._serialized_end=2197
  _globals['_QUERYDENOMTOERC20RESPONSE']._serialized_start=2199
  _globals['_QUERYDENOMTOERC20RESPONSE']._serialized_end=2264
  _globals['_QUERYDELEGATEKEYBYVALIDATORREQUEST']._serialized_start=2266
  _globals['_QUERYDELEGATEKEYBYVALIDATORREQUEST']._serialized_end=2329
  _globals['_QUERYDELEGATEKEYBYVALIDATORRESPONSE']._serialized_start=2331
  _globals['_QUERYDELEGATEKEYBYVALIDATORRESPONSE']._serialized_end=2419
  _globals['_QUERYDELEGATEKEYBYETHREQUEST']._serialized_start=2421
  _globals['_QUERYDELEGATEKEYBYETHREQUEST']._serialized_end=2472
  _globals['_QUERYDELEGATEKEYBYETHRESPONSE']._serialized_start=2474
  _globals['_QUERYDELEGATEKEYBYETHRESPONSE']._serialized_end=2562
  _globals['_QUERYDELEGATEKEYBYORCHESTRATORREQUEST']._serialized_start=2564
  _globals['_QUERYDELEGATEKEYBYORCHESTRATORREQUEST']._serialized_end=2633
  _globals['_QUERYDELEGATEKEYBYORCHESTRATORRESPONSE']._serialized_start=2635
  _globals['_QUERYDELEGATEKEYBYORCHESTRATORRESPONSE']._serialized_end=2723
  _globals['_QUERYPENDINGSENDTOETHREQUEST']._serialized_start=2725
  _globals['_QUERYPENDINGSENDTOETHREQUEST']._serialized_end=2779
  _globals['_QUERYPENDINGSENDTOETHRESPONSE']._serialized_start=2782
  _globals['_QUERYPENDINGSENDTOETHRESPONSE']._serialized_end=2942
  _globals['_QUERYLASTOBSERVEDBLOCKHEIGHTREQUEST']._serialized_start=2944
  _globals['_QUERYLASTOBSERVEDBLOCKHEIGHTREQUEST']._serialized_end=2981
  _globals['_QUERYLASTOBSERVEDBLOCKHEIGHTRESPONSE']._serialized_start=2983
  _globals['_QUERYLASTOBSERVEDBLOCKHEIGHTRESPONSE']._serialized_end=3069
  _globals['_QUERYLASTEVENTBLOCKHEIGHTBYADDRREQUEST']._serialized_start=3071
  _globals['_QUERYLASTEVENTBLOCKHEIGHTBYADDRREQUEST']._serialized_end=3128
  _globals['_QUERYLASTEVENTBLOCKHEIGHTBYADDRRESPONSE']._serialized_start=3130
  _globals['_QUERYLASTEVENTBLOCKHEIGHTBYADDRRESPONSE']._serialized_end=3193
  _globals['_QUERYPROJECTEDBATCHTIMEOUTHEIGHTREQUEST']._serialized_start=3195
  _globals['_QUERYPROJECTEDBATCHTIMEOUTHEIGHTREQUEST']._serialized_end=3236
  _globals['_QUERYPROJECTEDBATCHTIMEOUTHEIGHTRESPONSE']._serialized_start=3238
  _globals['_QUERYPROJECTEDBATCHTIMEOUTHEIGHTRESPONSE']._serialized_end=3304
  _globals['_QUERYBRIDGETOKENSREQUEST']._serialized_start=3306
  _globals['_QUERYBRIDGETOKENSREQUEST']._serialized_end=3332
  _globals['_QUERYBRIDGETOKENSRESPONSE']._serialized_start=3334
  _globals['_QUERYBRIDGETOKENSRESPONSE']._serialized_end=3413
  _globals['_QUERY']._serialized_start=3416
  _globals['_QUERY']._serialized_end=7224
# @@protoc_insertion_point(module_scope)