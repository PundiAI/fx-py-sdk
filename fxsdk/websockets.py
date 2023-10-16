import asyncio
import logging
import traceback
from random import random
from typing import Optional, Dict

import ujson as json
import websockets.client


class ReconnectingWebsocket:
    MAX_RECONNECTS: int = 5
    MAX_RECONNECT_SECONDS: int = 60
    MIN_RECONNECT_WAIT = 0.1
    TIMEOUT: int = 10
    PROTOCOL_VERSION: str = '1.0.0'

    def __init__(self, endpoint_url: str, loop, recv, retry_count: int = 5):
        self._loop = loop
        self._log = logging.getLogger(__name__)
        self._recv = recv
        self._reconnect_attempts: int = 0
        self._conn = None
        self._endpoint_url = endpoint_url
        self._connect_id: int = -1
        self._ping_timeout = 60
        self._retry_count: int = retry_count
        self._socket: Optional[websockets.client.WebSocketClientProtocol] = None

        self._connect()

    def _connect(self):
        self._conn = asyncio.ensure_future(self._run())

    def _get_ws_endpoint_url(self):
        return f"{self._endpoint_url}/websocket"

    async def _run(self):

        keep_waiting: bool = True

        self._log.info(f"connecting to {self._get_ws_endpoint_url()}")
        try:
            async with websockets.client.connect(self._get_ws_endpoint_url(), loop=self._loop) as socket:
                self._on_connect(socket)

                try:
                    while keep_waiting:
                        try:
                            evt = await asyncio.wait_for(self._socket.recv(), timeout=self._ping_timeout)
                        except asyncio.TimeoutError:
                            self._log.debug("no message in {} seconds".format(self._ping_timeout))
                            await self.send_keepalive()
                        except asyncio.CancelledError:
                            self._log.debug("cancelled error")
                            await self.ping()
                        else:
                            try:
                                evt_obj = json.loads(evt)
                                await self._recv(evt_obj)
                            except ValueError:
                                self._log.error("invalid json: {}".format(evt))
                except websockets.ConnectionClosed as e:
                    self._log.debug('conn closed:{}'.format(e))
                    await self._reconnect()
                except Exception as e:
                    self._log.debug('ws exception:{}'.format(e))
                    await self._reconnect()
        except Exception as e:
            self._log.info(f"websocket error: {e}")
            traceback.print_stack()

    def _on_connect(self, socket):
        self._socket = socket
        self._reconnect_attempts = 0

    async def _reconnect(self):
        await self.cancel()
        self._reconnect_attempts += 1
        if self._reconnect_attempts < self.MAX_RECONNECTS:

            self._log.debug(f"websocket reconnecting {self.MAX_RECONNECTS - self._reconnect_attempts} attempts left")
            reconnect_wait = self._get_reconnect_wait(self._reconnect_attempts)
            self._log.debug(f' waiting {reconnect_wait}')
            await asyncio.sleep(reconnect_wait)
            self._connect()
        else:
            # maybe raise an exception
            self._log.error(f"websocket could not reconnect after {self._reconnect_attempts} attempts")
            pass

    def _get_reconnect_wait(self, attempts: int) -> int:
        expo = 2 ** attempts
        return round(random() * min(self.MAX_RECONNECT_SECONDS, expo - 1) + 1)

    async def send_keepalive(self):
        msg = {"method": "keepAlive"}
        await self._socket.send(json.dumps(msg, ensure_ascii=False))

    async def send_message(self, msg, retry_count=0):
        if not self._socket:
            if retry_count < self._retry_count:
                await asyncio.sleep(1)
                await self.send_message(msg, retry_count + 1)
            else:
                self._log.info("Unable to send, not connected")
        else:
            await self._socket.send(json.dumps(msg, ensure_ascii=False))

    async def ping(self):
        await self._socket.ping()

    async def cancel(self):
        try:
            self._conn.cancel()
        except asyncio.CancelledError:
            pass


class WebsocketManagerBase:

    def __init__(self):
        self._conn = None
        self._log = logging.getLogger(__name__)

    @classmethod
    async def create(cls, endpoint_url: str, loop, callback=None):
        """Create a WebsocketManagerBase instance

        :param endpoint_url: node endpoint url
        :param loop: asyncio loop
        :param callback: async callback function to receive messages
        :return:
        """
        self = WebsocketManagerBase()
        loop = loop
        callback = callback if callback else self.receive
        self._conn = ReconnectingWebsocket(endpoint_url, recv=callback, loop=loop)
        return self

    async def receive(self, data: Dict):
        self._log.debug(f"received data: {data}")

    async def close(self):
        await self._conn.cancel()
