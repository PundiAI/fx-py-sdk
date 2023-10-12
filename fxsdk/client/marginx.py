from decimal import Decimal
from typing import Optional

from fxsdk.client.grpc import Client, GRPCBlockHeightHeader
from fxsdk.dec import dec_from_str
from fxsdk.msg.marginx import new_position_from_proto, new_order_from_proto, Order, Position, \
    new_pair_funding_rate_from_proto, PairFundingRate, OrderDepths, PairPrice, new_order_depths_from_proto, DecCoin

from fxsdk.x.marginx.oracle.v1.query_pb2 import QueryPriceRequest, QueryMarketRequest
from fxsdk.x.marginx.oracle.v1.types_pb2 import Market
from fxsdk.x.marginx.oracle.v1.query_pb2_grpc import QueryStub as OracleClient

from fxsdk.x.fx.dex.v1.funding_pb2 import Funding
from fxsdk.x.fx.dex.v1.query_pb2_grpc import QueryStub as DexClient
from fxsdk.x.fx.dex.v1.query_pb2 import QueryPositionReq, QueryOrderRequest, QueryOrdersRequest, QueryFundingReq, \
    QueryPairFundingRatesReq, QueryOrderbookReq, QueryMarkPriceReq


class MarginXClient(Client):

    def __init__(self, url: str = 'localhost:9090'):
        super().__init__(url)

    def query_dec_balance(self, address: str, denom: str, height: Optional[int] = 0) -> DecCoin:
        balance = self.query_balance(address, denom, height)
        return DecCoin(balance.denom, dec_from_str(balance.amount))

    def query_all_dec_balances(self, address: str, height: Optional[int] = 0) -> [DecCoin]:
        balances = self.query_all_balances(address, height)
        coins = []
        for balance in balances:
            coins.append(DecCoin(balance.denom, dec_from_str(balance.amount)))
        return coins

    def query_oracle_price(self, pair_id: str, height: Optional[int] = 0) -> Decimal:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = OracleClient(self.channel).Price(QueryPriceRequest(pair_id=pair_id), metadata=metadata)
        return dec_from_str(response.price)

    def query_oracle_prices(self, height: Optional[int] = 0) -> [PairPrice]:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = OracleClient(self.channel).Prices(QueryPriceRequest(), metadata=metadata)
        pair_prices = []
        for price in response.prices:
            pair_prices.append(PairPrice(price.pair_id, dec_from_str(price.price)))
        return pair_prices

    def query_oracle_market(self, pair_id: str, height: Optional[int] = 0) -> Market:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = OracleClient(self.channel).Market(QueryMarketRequest(pair_id=pair_id), metadata=metadata)
        return response.market

    def query_oracle_markets(self, height: Optional[int] = 0) -> [Market]:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = OracleClient(self.channel).Markets(QueryMarketRequest(), metadata=metadata)
        return response.markets

    def query_positions(self, owner: str, pair_id: str, height: Optional[int] = 0) -> [Position]:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = DexClient(self.channel).QueryPosition(QueryPositionReq(owner=owner, pair_id=pair_id),
                                                         metadata=metadata)
        positions = []
        for position in response.positions:
            positions.append(new_position_from_proto(position))
        return positions

    def query_order(self, order_id: str, height: Optional[int] = 0) -> Order:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = DexClient(self.channel).QueryOrder(QueryOrderRequest(order_id=order_id), metadata=metadata)
        order = new_order_from_proto(response.order)
        return order

    def query_orders(self, owner: str, pair_id: str, height: Optional[int] = 0) -> [Order]:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = DexClient(self.channel).QueryOrders(QueryOrdersRequest(owner=owner, pair_id=pair_id),
                                                       metadata=metadata)
        orders = []
        for order in response.orders:
            orders.append(new_order_from_proto(order))
        return orders

    def query_funding_info(self, height: Optional[int] = 0) -> Funding:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = DexClient(self.channel).QueryFunding(QueryFundingReq(), metadata=metadata)
        return response.funding

    def query_funding_rates(self, last_or_realtime: bool = True, height: Optional[int] = 0) -> [PairFundingRate]:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = DexClient(self.channel).QueryPairFundingRates(
            QueryPairFundingRatesReq(last_or_realtime=last_or_realtime), metadata=metadata)
        pair_funding_rates = []
        for rate in response.pair_funding_rates:
            pair_funding_rates.append(new_pair_funding_rate_from_proto(rate))
        return pair_funding_rates

    def query_order_depths(self, pair_id: str, height: Optional[int] = 0) -> OrderDepths:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = DexClient(self.channel).QueryOrderbook(QueryOrderbookReq(pair_id=pair_id), metadata=metadata)
        return new_order_depths_from_proto(response.Asks, response.Bids)

    def query_mark_price(self, paid_id: str, height: Optional[int] = 0) -> Decimal:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = DexClient(self.channel).QueryMarkPrice(QueryMarkPriceReq(pair_id=paid_id), metadata=metadata)
        if len(response.pair_mark_price) > 0:
            return dec_from_str(response.pair_mark_price[0].price)
        else:
            raise Exception("No mark price found for pair_id: {}".format(paid_id))

    def query_mark_prices(self, height: Optional[int] = 0) -> [PairPrice]:
        metadata = [(GRPCBlockHeightHeader, str(height))]
        response = DexClient(self.channel).QueryMarkPrice(QueryMarkPriceReq(query_all=True), metadata=metadata)
        pair_prices = []
        for price in response.pair_mark_price:
            pair_prices.append(PairPrice(price.pair_id, dec_from_str(price.price)))
        return pair_prices
