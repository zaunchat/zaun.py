#TODO: implments heartbeat task

import json
import typing
import asyncio
import aiohttp
import logging

log = logging.getLogger('itchat.websocket')

from itchat import constants

class WebSocketShard:
    def __init__(
        self,
        token: str,
        url: str,
        *,
        loop: typing.Optional[asyncio.AbstractEventLoop] = None,
    ) -> None:
        self.token = token
        "The token of the bot."
        
        self.url = url
        "The url of the shard."
        
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
        ]] = {}
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
        
        await self.send(constants.WSEvents.AUTHENTICATE, {
            "token": self.token,
        })
        
    async def send(self, opcode: str, payload: typing.Dict):
        "Coro: Send and serlize the payload to the websocket."
        
        payload = json.dumps({
            "event": str(opcode),
            **payload,
        })
        
        if opcode != constants.WSEvents.AUTHENTICATE and self.token in payload:
            payload = payload.replace(
                self.token, "TOKEN_REPLACED")
        
        await self.socket.send_str(payload)
            
    async def poll_event(self):
        async for message in self.socket:
            if message.type == aiohttp.WSMsgType.TEXT:
                payload = json.loads(message.data)
                
                if payload['event'] in self.handlers:
                    await self.handlers[
                        payload['event']](payload)
                    "Async: Call the handler of the event."
                    
            elif message.type == aiohttp.WSMsgType.ERROR:
                log.error('An error occurred')
            
    async def on_authenticated(self, payload):
        "Coro: a handler for the AUTHENTICATED event."
        self.is_connected = True
        
    async def on_pong(self, payload):
        "Coro: a handler for the pong event."
        self.last_pong_acked = True
        
    async def on_ready(self, payload):
        "Coro: a handler for the ready event."
        
        self.last_pong_acked = True
        
        #TODO: implement the ready event
        
        self.is_ready = True