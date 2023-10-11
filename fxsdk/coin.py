import re

from fxsdk.x.cosmos.base.v1beta1.coin_pb2 import Coin


def parse_coins(value: str) -> [Coin]:
    """Parse the coins.

    :param value: coins
    :raises RuntimeError: If unable to parse the value
    :return: coins
    """
    coins = []
    parts = value.split(',')
    for part in parts:
        part = part.strip()
        if part == "":
            continue
        coins.append(parse_coin(part))

    return coins


def parse_coin(value: str) -> Coin:
    match = re.match(r"(\d+.\d+)(\w+)", value)
    if match is None:
        raise RuntimeError(f"Unable to parse value {value}")

    # extract out the groups
    amount, denom = match.groups()
    return Coin(amount=amount, denom=denom)
