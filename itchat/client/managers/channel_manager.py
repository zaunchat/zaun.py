import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client

from itchat import schemas

class ChannelManager:
    def __init__(self, client: "Client") -> None:
        self.client = client
        "The client."
        
        self.cache: typing.Dict[int, schemas.Channel] = {}
        "The cache of the channels."
        
    def add(self, data: dict) -> None:
        """Add a channel to the cache."""
        
        channel: schemas.Channel = schemas.Channel.form_dict(data)
        self.cache[channel.id] = channel
        return channel
    
    def get(self, id: int) -> schemas.Channel:
        """Get a channel from the cache."""
        
        return self.cache.get(int(id), None)