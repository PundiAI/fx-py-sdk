from decimal import Decimal
from typing import NamedTuple

from fxsdk.dec import dec_from_str
from fxsdk.wallet.address import Address
from fxsdk.x.fx.dex.v1.position_pb2 import Position as PositionProto


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
    owner = Address(position.owner, prefix)
    direction = ""
    if str(position.direction) == '1':
        direction = "long"
    elif str(position.direction) == '2':
        direction = "short"
    return Position(
        int(position.id),
        owner.to_string(),
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
