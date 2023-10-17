import time
from typing import Dict

from fxsdk.client.http import HttpRpcClient, RPCException
from fxsdk.msg import new_tx_from_base64
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import Tx


class ScanException(Exception):
    pass


class ScanBlock(HttpRpcClient):
    def __init__(self, endpoint_url, block_interval_ms: int = 500):
        super().__init__(endpoint_url)
        self._start_block_height = -1
        self._block_interval_ms = block_interval_ms

    def start(self, start_block_height: int = -1):
        if start_block_height > 0:
            self._start_block_height = start_block_height
        else:
            status = self.get_status()
            if status.get('sync_info', {}).get('catching_up', True):
                raise ScanException("node is catching up")
            latest_block_height = status.get('sync_info', {}).get('latest_block_height', 1)
            self._start_block_height = int(latest_block_height)
        while True:
            try:
                block_result = self.get_block_results(self._start_block_height)
                txs_results = block_result.get('txs_results', [])
                txs_results = txs_results if txs_results else []
                txs = []
                if len(txs_results) > 0:
                    block = self.get_block(self._start_block_height)
                    base64_txs = block.get('block', {}).get('data', {}).get('txs', [])
                    for base64_tx in base64_txs:
                        tx = new_tx_from_base64(base64_tx)
                        txs.append(tx)
                block_events = block_result.get('finalize_block_events', [])
                block_height = block_result.get('height', 0)
                self.process_new_block(block_height, block_events, txs_results, txs)
                self._start_block_height += 1
            except RPCException as e:
                self._log.debug(f"rpc exception: {e}")
                continue
            time.sleep(self._block_interval_ms / 1000)

    def process_new_block(self, block_height: int, block_events: [Dict], txs_result: [Dict], txs: [Tx]):
        self._log.info(
            f"new block: height={block_height}, txs={len(txs)}, txs_result={len(txs_result)} events={len(block_events)}")
