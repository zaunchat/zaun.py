import json
import typing
import asyncio
import aiohttp
import logging
import time

log = logging.getLogger('itchat.websocket')

from itchat import constants
from itchat.client import errors

class WebSocketShard:
    def __init__(
        self,
        token: str,
        url: str,
        heartbeat_interval: float = 30.0,
        reconnect: bool = True,
        *,
        loop: typing.Optional[asyncio.AbstractEventLoop] = None,
    ) -> None:
        self.token = token
        "The token of the bot."
        
        self.url = url
        "The url of the shard."
        
        self.heartbeat_interval = heartbeat_interval
        "The heartbeat interval."
        
        self.reconnect = reconnect
        "Whether to reconnect the shard."
        
        self.loop = loop or asyncio.get_event_loop()
        "The event loop."
        
        self.heartbeat_task: typing.Optional[asyncio.Task] = None
        "The heartbeat task."
        
        self.heartbeat_interval: typing.Optional[float] = None
        "The heartbeat interval."
        
        self.last_ping_timestamp: typing.Optional[float] = None
        "The last ping timestamp."
        
        self.last_pong_acked: typing.Optional[bool] = False
        "The last pong timestamp."
        
        self.session: typing.Optional[aiohttp.ClientSession] = None
        "The session of the shard."
        
        self.socket: typing.Optional[aiohttp.ClientWebSocketResponse] = None
        "The socket of the shard."
        
        self.handlers: typing.Dict[str, typing.Union[
            typing.Callable, typing.Coroutine
        ]] = {
            "Authenticated": self.on_authenticated,
            "Pong": self.on_pong,
        }
        "The handlers of the shard."
        
        # State of the shard
        
        self.is_ready: bool = False
        self.is_connected: bool = False
        
    async def init(self):
        "Coro: Initialize the shard."
        self.session = aiohttp.ClientSession(
            loop=self.loop,
        )
        "The client session for the aiohttp."
        
        self.socket = await self.session.ws_connect(self.url)
        "Connect to the websocket."
        
        await self.send({
            "event": "Authenticate",
            "token": self.token,
        })
        
        await self.poll_event()
        
    async def send(self, payload: typing.Dict):
        "Coro: Send and serlize the payload to the websocket."
        print(payload)
        await self.socket.send_str(json.dumps(payload))
        
    # async def start_sending_heartbeat(self):
    #     "Coro: Start the heartbeat."
        
    #     if not self.heartbeat_interval:
    #         raise errors.NoHeartbeatIntervalError('Heartbeat interval is not set.', self)
        
    #     self.heartbeat_task = self.loop.create_task(
    #         self.send_heartbeat())
        
    # async def send_heartbeat(self):
    #     "Coro: Send the heartbeat."
        
    #     while True:
    #         if not self.last_pong_acked:
    #             log.debug('Did not receive a pong ack last time.');
    #             if self.reconnect:
    #                 log.debug('Reconnecting...');
                    
    #                 await self.reconnect_shard()
                
    #         now = time.time()
    #         await self.send(constants.WSEvents.PING, {"data": now})
    #         self.last_pong_acked = False
    #         self.last_ping_timestamp = now
            
    #         await asyncio.sleep(self.heartbeat_interval)
            
    async def poll_event(self):
        async for message in self.socket:
            if message.type == aiohttp.WSMsgType.TEXT:
                payload = json.loads(message.data)
                
                if payload['event'] in self.handlers:
                    await self.handlers[
                        payload['event']](payload=payload)
                    "Async: Call the handler of the event."
                    
            elif message.type == aiohttp.WSMsgType.ERROR:
                log.error('An error occurred')
            
    async def on_authenticated(self, payload):
        "Coro: a handler for the AUTHENTICATED event."
        self.is_connected = True
        
    async def on_pong(self, payload):
        "Coro: a handler for the pong event."
        self.last_pong_acked = True