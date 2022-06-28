import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client

from itchat import schemas

class RoleManager:
    def __init__(self, client: "Client") -> None:
        self.client = client
        "The client."
        
        self.cache: typing.Dict[int, schemas.RatelimitInfo] = {}
        "The cache of the roles."
        
    def add(self, data: dict) -> "schemas.Role":
        """Add a role to the cache."""
        
        role: schemas.Role = schemas.Role.form_dict(data)
        self.cache[role.id] = role
        return role
    
    def get(self, id: str) -> "schemas.Role":
        """Get a role from the cache."""
        
        return self.cache.get(str(id), None)