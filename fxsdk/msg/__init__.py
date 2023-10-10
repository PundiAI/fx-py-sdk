from google.protobuf.any_pb2 import Any
from decimal import Decimal

from fxsdk.x.cosmos.bank.v1beta1.tx_pb2 import MsgSend
from fxsdk.x.cosmos.base.v1beta1.coin_pb2 import Coin
from fxsdk.x.fx.dex.v1.order_pb2 import Direction
from fxsdk.x.fx.dex.v1.tx_pb2 import MsgCreateOrder, MsgCancelOrder, MsgClosePosition, MsgAddMargin

DEFAULT_DEC = 1000000


def dec_to_str(amount: Decimal) -> str:
    amount = amount * Decimal(DEFAULT_DEC)
    amount = str(amount)
    return amount.split('.', 1)[0]


def new_msg_send(from_address: str, to_address: str, amount: [Coin]) -> Any:
    msg = MsgSend(
        from_address=from_address,
        to_address=to_address,
        amount=amount,
    )
    msg_any = Any(
        type_url='/cosmos.bank.v1beta1.MsgSend',
        value=msg.SerializeToString(),
    )
    return msg_any


def new_msg_create_order(owner: str, pair_id: str, direction: Direction, price: Decimal, base_quantity: Decimal,
                         leverage: int) -> Any:
    msg = MsgCreateOrder(
        owner=owner,
        pair_id=pair_id,
        direction=direction,
        price=dec_to_str(price),
        base_quantity=dec_to_str(base_quantity),
        leverage=leverage,
    )
    msg_any = Any(
        type_url='/fx.dex.v1.MsgCreateOrder',
        value=msg.SerializeToString(),
    )
    return msg_any


def new_msg_cancel_order(owner: str, order_id: str) -> Any:
    msg = MsgCancelOrder(owner=owner, order_id=order_id)
    msg_any = Any(
        type_url='/fx.dex.v1.MsgCancelOrder',
        value=msg.SerializeToString(),
    )
    return msg_any


def new_msg_close_position(owner: str, pair_id: str, position_id: str, price: Decimal, base_quantity: Decimal,
                           full_close: bool, market_close=False):
    msg = MsgClosePosition(
        owner=owner,
        pair_id=pair_id,
        position_id=position_id,
        price=dec_to_str(price),
        base_quantity=dec_to_str(base_quantity),
        full_close=full_close,
        market_close=market_close,
    )

    msg_any = Any(
        type_url='/fx.dex.v1.MsgClosePosition',
        value=msg.SerializeToString(),
    )
    return msg_any


def new_msg_add_margin(owner: str, pair_id: str, position_id: str, amount: Decimal):
    msg = MsgAddMargin(
        owner=owner,
        pair_id=pair_id,
        position_id=position_id,
        margin=dec_to_str(amount),
    )
    msg_any = Any(
        type_url='/fx.dex.v1.MsgAddMargin',
        value=msg.SerializeToString(),
    )
    return msg_any
