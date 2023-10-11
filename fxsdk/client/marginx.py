from decimal import Decimal

from fxsdk.client.grpc import Client
from fxsdk.dec import dec_from_str
from fxsdk.msg.dex import new_position_from_proto, new_order_from_proto, Order, Position, \
    new_pair_funding_rate_from_proto, PairFundingRate, OrderDepths, PairPrice, new_order_depths_from_proto

from fxsdk.x.marginx.oracle.v1.query_pb2 import QueryPriceRequest, QueryMarketRequest
from fxsdk.x.marginx.oracle.v1.types_pb2 import Market
from fxsdk.x.marginx.oracle.v1.query_pb2_grpc import QueryStub as OracleClient

from fxsdk.x.fx.dex.v1.funding_pb2 import Funding
from fxsdk.x.fx.dex.v1.query_pb2_grpc import QueryStub as DexClient
from fxsdk.x.fx.dex.v1.query_pb2 import QueryPositionReq, QueryOrderRequest, QueryOrdersRequest, QueryFundingReq, \
    QueryPairFundingRatesReq, QueryOrderbookReq, QueryMarkPriceReq


class MxClient(Client):

    def __init__(self, url: str = 'localhost:9090'):
        super().__init__(url)

    def query_oracle_price(self, pair_id: str) -> Decimal:
        response = OracleClient(self.channel).Price(QueryPriceRequest(pair_id=pair_id))
        return dec_from_str(response.price)

    def query_oracle_prices(self):  # TODO: need fix return type
        response = OracleClient(self.channel).Prices(QueryPriceRequest())
        return response.prices

    def query_oracle_market(self, pair_id: str) -> Market:
        response = OracleClient(self.channel).Market(QueryMarketRequest(pair_id=pair_id))
        return response.market

    def query_oracle_markets(self) -> [Market]:
        response = OracleClient(self.channel).Markets(QueryMarketRequest())
        return response.markets

    def query_positions(self, owner: str, pair_id: str) -> [Position]:
        positions = []
        response = DexClient(self.channel).QueryPosition(QueryPositionReq(owner=owner, pair_id=pair_id))
        for position in response.positions:
            positions.append(new_position_from_proto(position))
        return positions

    def query_order(self, order_id: str) -> Order:
        response = DexClient(self.channel).QueryOrder(QueryOrderRequest(order_id=order_id))
        order = new_order_from_proto(response.order)
        return order

    def query_orders(self, owner: str, pair_id: str) -> [Order]:
        orders = []
        response = DexClient(self.channel).QueryOrders(QueryOrdersRequest(owner=owner, pair_id=pair_id))
        for order in response.orders:
            orders.append(new_order_from_proto(order))
        return orders

    def query_funding_info(self) -> Funding:
        response = DexClient(self.channel).QueryFunding(QueryFundingReq())
        return response.funding

    def query_funding_rates(self, last_or_realtime: bool = True) -> [PairFundingRate]:
        response = DexClient(self.channel).QueryPairFundingRates(
            QueryPairFundingRatesReq(last_or_realtime=last_or_realtime))
        pair_funding_rates = []
        for rate in response.pair_funding_rates:
            pair_funding_rates.append(new_pair_funding_rate_from_proto(rate))
        return pair_funding_rates

    def query_order_depths(self, pair_id: str) -> OrderDepths:
        response = DexClient(self.channel).QueryOrderbook(QueryOrderbookReq(pair_id=pair_id))
        return new_order_depths_from_proto(response.Asks, response.Bids)

    def query_mark_price(self, paid_id: str) -> Decimal:
        response = DexClient(self.channel).QueryMarkPrice(QueryMarkPriceReq(pair_id=paid_id))
        if len(response.pair_mark_price) > 0:
            return dec_from_str(response.pair_mark_price[0].price)
        else:
            raise Exception("No mark price found for pair_id: {}".format(paid_id))

    def query_mark_prices(self) -> [PairPrice]:
        response = DexClient(self.channel).QueryMarkPrice(QueryMarkPriceReq(query_all=True))
        pair_prices = []
        for price in response.pair_mark_price:
            pair_prices.append(PairPrice(price.pair_id, dec_from_str(price.price)))
        return pair_prices
