import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client

from itchat import schemas

class InviteManager:
    def __init__(self, client: "Client") -> None:
        self.client = client
        "The client."
        
        self.cache: typing.Dict[int, schemas.Invite] = {}
        "The cache of the invites."
        
    def add(self, data: dict) -> None:
        """Add a invite to the cache."""
        
        invite: schemas.Invite = schemas.Invite.form_dict(data)
        self.cache[invite.id] = invite
        return invite