import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client

from itchat import schemas

class MemberManager:
    def __init__(self, client: "Client") -> None:
        self.client = client
        "The client."
        
        self.cache: typing.Dict[int, schemas.Member] = {}
        "The cache of the memeber."
        
    def add(self, data: dict) -> "schemas.Member":
        """Add a member to the cache."""
        
        member: schemas.Member = schemas.Member.form_dict(data)
        self.cache[member.id] = member
        return member