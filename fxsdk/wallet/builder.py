from google.protobuf.any_pb2 import Any

from fxsdk.x.cosmos.base.v1beta1.coin_pb2 import Coin
from fxsdk.x.cosmos.tx.signing.v1beta1.signing_pb2 import SIGN_MODE_DIRECT
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import AuthInfo
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import Fee
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import ModeInfo
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import SignDoc
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import SignerInfo
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import Tx
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import TxBody
from fxsdk.wallet.address import Address
from fxsdk.wallet.key import PrivateKey, DEFAULT_DERIVATION_PATH, mnemonic_to_privkey


class TxBuilder:
    def __init__(self, private_key: PrivateKey,
                 chain_id: str = '',
                 gas_price: Coin = Coin(amount='0', denom="FX")):
        self.chain_id = chain_id
        if gas_price.amount != '0' and gas_price.denom == '':
            raise Exception('gas price denom can not be empty')
        self.gas_price = gas_price
        self._private_key = private_key
        self._memo = ''

    @classmethod
    def from_mnemonic(cls, mnemonic: str, path: str = DEFAULT_DERIVATION_PATH,
                      chain_id: str = '',
                      gas_price: Coin = Coin(amount='0', denom="FX")):
        private_key = mnemonic_to_privkey(mnemonic, path)
        return cls(private_key=private_key, chain_id=chain_id, gas_price=gas_price)

    def with_memo(self, memo: str):
        self._memo = memo

    def address(self) -> str:
        return self._private_key.to_address()

    def acc_address(self):
        addr = Address(self.address())
        return addr.to_bytes()

    def sign(self, msgs: [Any], fee: Fee, account_number: int, sequence: int, timeout_height: int = 0) -> Tx:
        tx_body = TxBody(messages=msgs, memo=self._memo,
                         timeout_height=timeout_height)
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
