import json
import logging

import websocket


class Websocket:

    def __init__(self, wss_url: str, event: bytes):
        self.wss_url = wss_url
        self.event = event
        self.ws_block = None
        self.subscribe()

    def _get_ws_endpoint_url(self):
        return f"{self.wss_url}websocket"

    def on_error(self, error):
        global reconnect_block_count
        if type(error) == ConnectionRefusedError or \
                type(error) == ConnectionResetError or \
                type(error) == websocket._exceptions.WebSocketConnectionClosedException:
            reconnect_block_count += 1
            if reconnect_block_count < 10:
                self.subscribe()
        else:
            print("websocket disconnected", error)

    def on_message(self, message):
        msg = json.loads(message)
        print(msg)

    def on_open(self):
        logging.info("connection to node...")
        self.ws_block.send(self.event)

    def on_close(self):
        logging.info("connection to node websocket is closed")

    def subscribe(self):
        websocket.enableTrace(True)
        logging.info(self._get_ws_endpoint_url())
        self.ws_block = websocket.WebSocketApp(self._get_ws_endpoint_url(),
                                               on_message=self.on_message,
                                               on_error=self.on_error,
                                               on_close=self.on_close,
                                               on_open=self.on_open)
        try:
            self.ws_block.run_forever()
        except KeyboardInterrupt:
            self.ws_block.close()
        except:
            self.ws_block.close()
