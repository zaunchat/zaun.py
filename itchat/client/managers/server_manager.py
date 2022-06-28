import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client

from itchat import schemas

class ServerManager:
    def __init__(self, client: "Client") -> None:
        self.client = client
        "The client."
        
        self.cache: typing.Dict[int, schemas.Server] = {}
        "The cache of the servers."
        
    def add(self, data: dict) -> None:
        """Add a server to the cache."""
        
        server: schemas.Server = schemas.Server.form_dict(data)
        self.cache[server.id] = server
        return server
    
    def get(self, id: str) -> schemas.Server:
        """Get a server from the cache."""
        
        return self.cache.get(str(id), None)