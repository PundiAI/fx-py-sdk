from fxsdk.client.grpc_client import Client

from fxsdk.x.marginx.oracle.v1.query_pb2 import QueryPriceRequest, QueryMarketRequest
from fxsdk.x.marginx.oracle.v1.query_pb2_grpc import QueryStub as OracleClient


class MxClient(Client):

    def __init__(self, url: str = 'localhost:9090'):
        super().__init__(url)

    def query_oracle_price(self, pair_id: str):
        response = OracleClient(self.channel).Price(QueryPriceRequest(pair_id=pair_id))
        return response.price

    def query_oracle_prices(self):
        response = OracleClient(self.channel).Prices(QueryPriceRequest())
        return response.prices

    def query_oracle_market(self, pair_id: str):
        response = OracleClient(self.channel).Market(QueryMarketRequest(pair_id=pair_id))
        return response.market

    def query_oracle_markets(self):
        response = OracleClient(self.channel).Markets(QueryMarketRequest())
        return response.markets
