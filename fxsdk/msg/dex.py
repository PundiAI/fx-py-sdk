from datetime import datetime
from decimal import Decimal
from typing import NamedTuple, Iterable

from fxsdk.coin import parse_coin
from fxsdk.dec import dec_from_str
from fxsdk.wallet.address import Address
from fxsdk.x.fx.dex.v1.position_pb2 import Position as PositionProto
from fxsdk.x.fx.dex.v1.order_pb2 import Order as OrderProto


class Position(NamedTuple):
    Id: int
    Owner: str
    PairId: str
    Direction: str
    EntryPrice: Decimal
    MarkPrice: Decimal
    LiquidationPrice: Decimal
    BaseQuantity: Decimal
    Margin: Decimal
    Leverage: int
    UnrealizedPnl: Decimal
    MarginRate: Decimal
    InitialMargin: Decimal
    PendingOrderQuantity: Decimal


def new_position_from_proto(position: PositionProto, prefix: str = 'mx'):
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
    Id: str
    Owner: str
    PairId: str
    Direction: str
    Price: Decimal
    BaseQuantity: Decimal
    QuoteQuantity: Decimal
    FilledQuantity: Decimal
    FilledAvgPrice: Decimal
    Leverage: int
    Status: str
    OrderType: str
    CostFee: Decimal
    LockedFee: Decimal
    FeeDenom: str


def new_order_from_proto(order: OrderProto, prefix: str = 'mx'):
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
