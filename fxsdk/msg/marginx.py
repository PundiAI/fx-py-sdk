from datetime import datetime
from decimal import Decimal
from typing import NamedTuple

from fxsdk.coin import parse_coin
from fxsdk.dec import dec_from_str
from fxsdk.wallet.address import Address
from fxsdk.x.fx.dex.v1.funding_pb2 import PairFundingRate as PairFundingRateProto
from fxsdk.x.fx.dex.v1.order_pb2 import Order as OrderProto
from fxsdk.x.fx.dex.v1.position_pb2 import Position as PositionProto
from fxsdk.x.fx.dex.v1.match_pb2 import OrderDepth as OrderDepthProto


class Position(NamedTuple):
    id: int
    owner: str
    pair_id: str
    direction: str
    entry_price: Decimal
    mark_price: Decimal
    liquidation_price: Decimal
    base_quantity: Decimal
    margin: Decimal
    leverage: int
    unrealized_pnl: Decimal
    margin_rate: Decimal
    initial_margin: Decimal
    pending_order_quantity: Decimal


def new_position_from_proto(position: PositionProto, prefix: str = 'mx') -> Position:
    direction = ""
    if str(position.direction) == '1':
        direction = "long"
    elif str(position.direction) == '2':
        direction = "short"
    return Position(
        int(position.id),
        Address(position.owner, prefix).to_string(),
        position.pair_id,
        direction,
        dec_from_str(position.entry_price),
        dec_from_str(position.mark_price),
        dec_from_str(position.liquidation_price),
        dec_from_str(position.base_quantity),
        dec_from_str(position.margin),
        position.leverage,
        dec_from_str(position.unrealized_pnl),
        dec_from_str(position.margin_rate),
        dec_from_str(position.initial_margin),
        dec_from_str(position.pending_order_quantity)
    )


class Order(NamedTuple):
    id: str
    owner: str
    pair_id: str
    direction: str
    price: Decimal
    base_quantity: Decimal
    quote_quantity: Decimal
    filled_quantity: Decimal
    filled_avg_price: Decimal
    leverage: int
    status: str
    order_type: str
    cost_fee: Decimal
    locked_fee: Decimal
    fee_denom: str


def new_order_from_proto(order: OrderProto, prefix: str = 'mx') -> Order:
    cost_fee_coin = parse_coin(order.cost_fee)
    locked_fee_coin = parse_coin(order.locked_fee)
    fee_denom = cost_fee_coin.denom
    if cost_fee_coin.denom == '':
        fee_denom = locked_fee_coin.denom
    return Order(
        order.id,
        Address(order.owner, prefix).to_string(),
        order.pair_id,
        str(order.direction),
        dec_from_str(order.price),
        dec_from_str(order.base_quantity),
        dec_from_str(order.quote_quantity),
        dec_from_str(order.filled_quantity),
        dec_from_str(order.filled_avg_price),
        order.leverage,
        str(order.status),
        str(order.order_type),
        dec_from_str(cost_fee_coin.amount),
        dec_from_str(locked_fee_coin.amount),
        fee_denom,
    )


class PairFundingRate(NamedTuple):
    pair_id: str
    funding_rate: Decimal
    funding_time: datetime


def new_pair_funding_rate_from_proto(pair_funding_rate: PairFundingRateProto) -> PairFundingRate:
    return PairFundingRate(
        pair_funding_rate.pair_id,
        dec_from_str(pair_funding_rate.funding_rate),
        datetime.fromtimestamp(pair_funding_rate.funding_time)
    )


class OrderDepth(NamedTuple):
    price: Decimal
    quantity: Decimal


def new_order_depth_from_proto(order_depth: OrderDepthProto) -> OrderDepth:
    return OrderDepth(
        dec_from_str(order_depth.price),
        dec_from_str(order_depth.quantity),
    )


class OrderDepths(NamedTuple):
    asks: [OrderDepth]
    bids: [OrderDepth]


def new_order_depths_from_proto(asks: [OrderDepthProto], bids: [OrderDepthProto]) -> OrderDepths:
    return OrderDepths(
        [new_order_depth_from_proto(ask) for ask in asks],
        [new_order_depth_from_proto(bid) for bid in bids],
    )


class PairPrice(NamedTuple):
    pair_id: str
    price: Decimal


class DecCoin(NamedTuple):
    denom: str
    amount: Decimal
