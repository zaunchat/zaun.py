import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client

from itchat import schemas

class MessageManager:
    def __init__(self, client: "Client") -> None:
        self.client = client
        "The client"
        
        self.cache: typing.Dict[int, schemas.Message] = {}
        "The cache of the messages."
        
    def add(self, data: dict) -> "schemas.Message":
        """Add a channel to the cache."""
        
        message: schemas.Message = schemas.Message.form_dict(data)
        self.cache[message.id] = message
        return message
    
    def get(self, id: int):
        return self.cache.get(int(id), None)