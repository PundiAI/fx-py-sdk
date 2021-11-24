# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from x.fx.erc20.v1 import query_pb2 as fx_dot_erc20_dot_v1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TokenPairs = channel.unary_unary(
                '/fx.erc20.v1.Query/TokenPairs',
                request_serializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairsRequest.SerializeToString,
                response_deserializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairsResponse.FromString,
                )
        self.TokenPair = channel.unary_unary(
                '/fx.erc20.v1.Query/TokenPair',
                request_serializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairRequest.SerializeToString,
                response_deserializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairResponse.FromString,
                )
        self.Params = channel.unary_unary(
                '/fx.erc20.v1.Query/Params',
                request_serializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
                response_deserializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
                )
        self.DenomAliases = channel.unary_unary(
                '/fx.erc20.v1.Query/DenomAliases',
                request_serializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryDenomAliasesRequest.SerializeToString,
                response_deserializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryDenomAliasesResponse.FromString,
                )
        self.AliasDenom = channel.unary_unary(
                '/fx.erc20.v1.Query/AliasDenom',
                request_serializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryAliasDenomRequest.SerializeToString,
                response_deserializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryAliasDenomResponse.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def TokenPairs(self, request, context):
        """Retrieves registered token pairs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TokenPair(self, request, context):
        """Retrieves a registered token pair
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params retrieves the erc20 module params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DenomAliases(self, request, context):
        """Retrieves registered denom aliases
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AliasDenom(self, request, context):
        """Retrieves registered alias denom
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TokenPairs': grpc.unary_unary_rpc_method_handler(
                    servicer.TokenPairs,
                    request_deserializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairsRequest.FromString,
                    response_serializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairsResponse.SerializeToString,
            ),
            'TokenPair': grpc.unary_unary_rpc_method_handler(
                    servicer.TokenPair,
                    request_deserializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairRequest.FromString,
                    response_serializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairResponse.SerializeToString,
            ),
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryParamsRequest.FromString,
                    response_serializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
            'DenomAliases': grpc.unary_unary_rpc_method_handler(
                    servicer.DenomAliases,
                    request_deserializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryDenomAliasesRequest.FromString,
                    response_serializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryDenomAliasesResponse.SerializeToString,
            ),
            'AliasDenom': grpc.unary_unary_rpc_method_handler(
                    servicer.AliasDenom,
                    request_deserializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryAliasDenomRequest.FromString,
                    response_serializer=fx_dot_erc20_dot_v1_dot_query__pb2.QueryAliasDenomResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fx.erc20.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def TokenPairs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.erc20.v1.Query/TokenPairs',
            fx_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairsRequest.SerializeToString,
            fx_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TokenPair(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.erc20.v1.Query/TokenPair',
            fx_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairRequest.SerializeToString,
            fx_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.erc20.v1.Query/Params',
            fx_dot_erc20_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
            fx_dot_erc20_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DenomAliases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.erc20.v1.Query/DenomAliases',
            fx_dot_erc20_dot_v1_dot_query__pb2.QueryDenomAliasesRequest.SerializeToString,
            fx_dot_erc20_dot_v1_dot_query__pb2.QueryDenomAliasesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AliasDenom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.erc20.v1.Query/AliasDenom',
            fx_dot_erc20_dot_v1_dot_query__pb2.QueryAliasDenomRequest.SerializeToString,
            fx_dot_erc20_dot_v1_dot_query__pb2.QueryAliasDenomResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
