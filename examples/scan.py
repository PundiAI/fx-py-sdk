import logging.config

import yaml

from fxsdk.client.scan import ScanBlock

if __name__ == '__main__':
    logging.config.dictConfig(yaml.safe_load(open('../.logging.yaml', 'r')))
    rpc_url = "http://127.0.0.1:26657"
    ws_client = ScanBlock(endpoint_url=rpc_url)
    ws_client.start()
