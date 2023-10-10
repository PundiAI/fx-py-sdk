import bech32

DEFAULT_BECH32_PREFIX = "fx"


class Address:
    def __init__(self, addr, prefix: str = DEFAULT_BECH32_PREFIX):
        self._prefix = prefix
        if type(addr) is str:
            _, data = bech32.bech32_decode(addr)
            self._data = data
        elif type(addr) is bytes:
            self._data = bech32.convertbits(addr, 8, 5)
        else:
            raise Exception('invalid address')

    def to_string(self, prefix: str = None) -> str:
        prefix = self._prefix if prefix is None else prefix
        return bech32.bech32_encode(prefix, self._data)

    def to_bytes(self) -> bytes:
        return bytes(bech32.convertbits(self._data, 5, 8, False))
