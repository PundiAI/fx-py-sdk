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

        match = re.match(r"(\d+.\d+)(\w+)", part)
        if match is None:
            raise RuntimeError(f"Unable to parse value {part}")

        # extract out the groups
        amount, denom = match.groups()
        coins.append(Coin(amount=amount, denom=denom))

    return coins
