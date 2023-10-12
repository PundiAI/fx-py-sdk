from google.protobuf.any_pb2 import Any

from fxsdk.wallet.address import DEFAULT_BECH32_PREFIX, Address
from fxsdk.wallet.key import PrivateKey, ETH_DERIVATION_PATH, mnemonic_to_privkey, ETHSECP256K1_KEY_TYPE
from fxsdk.x.cosmos.base.v1beta1.coin_pb2 import Coin
from fxsdk.x.cosmos.tx.signing.v1beta1.signing_pb2 import SIGN_MODE_DIRECT
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import AuthInfo
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import Fee
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import ModeInfo
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import SignDoc
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import SignerInfo
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import Tx
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import TxBody


class TxBuilder:
    def __init__(self, private_key: PrivateKey,
                 chain_id: str = '',
                 gas_price: Coin = Coin(amount='0', denom=''),
                 prefix: str = DEFAULT_BECH32_PREFIX):
        self._prefix = prefix
        self.chain_id = chain_id
        if gas_price.amount != '0' and gas_price.denom == '':
            raise Exception('gas price denom can not be empty')
        self.gas_price = gas_price
        self._private_key = private_key
        self._memo = ''

    @classmethod
    def from_mnemonic(cls, mnemonic: str, path: str = ETH_DERIVATION_PATH,
                      chain_id: str = '',
                      gas_price: Coin = Coin(amount='0', denom=''),
                      prefix: str = DEFAULT_BECH32_PREFIX,
                      key_type: str = ETHSECP256K1_KEY_TYPE):
        private_key = mnemonic_to_privkey(mnemonic=mnemonic, path=path, key_type=key_type)
        return cls(private_key=private_key, chain_id=chain_id, gas_price=gas_price, prefix=prefix)

    def with_memo(self, memo: str):
        self._memo = memo

    def has_gas_price(self) -> bool:
        return self.gas_price.denom != ''

    def with_gas_price(self, gas_prices: [Coin]):
        if len(gas_prices) == 0:
            raise Exception("gas prices is empty")
        if self.gas_price.denom == '':
            self.gas_price = gas_prices[0]
            return
        for item in gas_prices:
            if item.denom == self.gas_price.denom:
                self.gas_price = item
        if self.has_gas_price() is False:
            raise Exception("invalid gas price")

    def from_address(self, prefix: str = None) -> Address:
        prefix = self._prefix if prefix is None else prefix
        return self._private_key.to_address(prefix=prefix)

    def sign(self, msgs: [Any], fee: Fee, account_number: int, sequence: int, timeout_height: int = 0) -> Tx:
        tx_body = TxBody(messages=msgs, memo=self._memo, timeout_height=timeout_height)
        tx_body_bytes = tx_body.SerializeToString()

        single = ModeInfo.Single(mode=SIGN_MODE_DIRECT)
        mode_info = ModeInfo(single=single)
        pub_key_any = self._private_key.to_public_key().to_secp256k1_any()

        signer_info = SignerInfo(
            public_key=pub_key_any, mode_info=mode_info, sequence=sequence)
        auth_info = AuthInfo(signer_infos=[signer_info], fee=fee)
        auth_info_bytes = auth_info.SerializeToString()

        sign_doc = SignDoc(body_bytes=tx_body_bytes,
                           auth_info_bytes=auth_info_bytes,
                           chain_id=self.chain_id,
                           account_number=account_number)
        sign_doc_bytes = sign_doc.SerializeToString()
        signature = self._private_key.sign(sign_doc_bytes)
        return Tx(body=tx_body, auth_info=auth_info, signatures=[signature])
