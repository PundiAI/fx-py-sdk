from decimal import Decimal

DEFAULT_DEC = 1000000


def dec_to_str(amount: Decimal) -> str:
    amount = amount * Decimal(DEFAULT_DEC)
    amount = str(amount)
    return amount.split('.', 1)[0]


def dec_from_str(amount: str) -> Decimal:
    amount = Decimal(amount) / Decimal(DEFAULT_DEC)
    return amount
