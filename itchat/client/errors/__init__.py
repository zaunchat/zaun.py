import typing

if typing.TYPE_CHECKING:
    from itchat.client import websocket

class BaseError(Exception):
    pass

class NoHeartbeatIntervalError(BaseError):
    def __init__(
        self,
        message: str, 
        shard: "websocket.WebSocketShard"
    ) -> None:
        self.message = message
        self.shard = shard
        
__all__ = (
    "BaseError",
    "NoHeartbeatIntervalError",
)