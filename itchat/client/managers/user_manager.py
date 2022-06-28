import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client

from itchat import schemas

class UserManager:
    def __init__(self, client: "Client") -> None:
        self.client = client
        "The client."
        
        self.cache: typing.Dict[int, schemas.User] = {}
        "The cache of the user."
        
    def add(self, data: dict) -> "schemas.User":
        """Add a user to the cache."""
        
        user: schemas.User = schemas.User.form_dict(data)
        self.cache[user.id] = user
        return user
    
    def get(self, id: str) -> "schemas.User":
        """Get a user from the cache."""
        
        return self.cache.get(str(id), None)