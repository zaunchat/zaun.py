import typing
import asyncio
import signal
import collections
import functools

from itchat.constants import default_client_options
from itchat.client import websocket
from itchat.client.managers import (
    ChannelManager,
    InviteManager,
    MemberManager,
    RoleManager,
    MessageManager,
    ServerManager,
    UserManager
)
from itchat.schemas import base
from itchat.client.actions import get_actions

Callable = typing.Union[typing.Callable, typing.Coroutine]
actions = get_actions()

class Client:
    """
    The main client of ItChat bots. It manage both gateway connection and RESTful API.
    It's also manage the cache that comes from the gateway and the RESTful API.
    """
    def __init__(
        self,
        loop: typing.Optional[asyncio.AbstractEventLoop] = None,
        *,
        **options
    ) -> None:
        self.loop = loop or asyncio.get_event_loop()
        "The event loop."
        
        self.options = (
            default_client_options if not options else options
        )
        "The options of the client."
        
        self.listeners: typing.Dict[str, typing.List[Callable]] = collections.defaultdict(list)
        "The listeners of the client."
        
        # Managers
        
        self.channels = ChannelManager(self)
        self.invites = InviteManager(self)
        self.members = MemberManager(self)
        self.roles = RoleManager(self)
        self.messages = MessageManager(self)
        self.servers = ServerManager(self)
        self.users = UserManager(self)
        
        base.APIObject.set_client(self)
        "The client of the APIObject."
        
    def listen(self, func: Callable = None, /, *, event: str = None):
        """
        Listen the event.
        """
        
        def deco(func: Callable):
            self.listeners[event].append(func)
            "Add the listener to the listeners."
            
            return func
        
        if func is None:
            return deco
        else:
            self.listeners[func.__name__].append(func)
            "Add the listener to the listeners."
            
            return func
        
    async def emit(self, event: str, *args, **kwargs):
        """
        Emit the event.
        """
        
        events = [
            event(*args, **kwargs) for event in self.listeners[event]
        ]
        
        await asyncio.gather(*events)
        "Gather the events."
        
    async def start(self, token: str):
        self.ws = websocket.WebSocketShard(
            token=token,
            url=self.options['ws_url'],
            loop=self.loop,
        )
        
        
        for event, action in actions.values():
            self.ws.handlers[event] = functools.partial(
                action, client=self, shard=self.ws)
            
        # TODO: implement the actions to the gateway.
        
        await self.ws.init()
        
    def login(self, token: str, *, asyncio_debug=False, os_interrupt=False):
        """
        Login the client.
        """
        self.loop.run_until_complete(
            self.start(token)
        )
        
        if asyncio_debug:
            self.loop.set_debug(True)
        
        if os_interrupt:
            self.loop.add_signal_handler(
                signal.SIGINT,
                self.loop.stop,
            )
        
        self.loop.run_forever()
        self.loop.close()
        
            
        
        