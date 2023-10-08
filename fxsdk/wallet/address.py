import bech32

DEFAULT_BECH32_HRP = "fx"


class Address:
    def __init__(self, addr):
        if type(addr) == str:
            _, data = bech32.bech32_decode(addr)
            self._data = data
        elif type(addr) == bytes:
            self._data = bech32.convertbits(addr, 8, 5)
        else:
            raise Exception('invalid address')

    def to_string(self, hrp: str = DEFAULT_BECH32_HRP) -> str:
        return bech32.bech32_encode(hrp, self._data)

    def to_bytes(self) -> bytes:
        return bytes(bech32.convertbits(self._data, 5, 8, False))

