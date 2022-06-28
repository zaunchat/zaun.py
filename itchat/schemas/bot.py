from dataclasses import dataclass
from itchat.schemas import base

@dataclass
class Bot(base.APIObject):
    """
    The ratelimit class.
    """
    
    __slots__ = 'username', 'verified', 'id', 'owner_id'
    
    username: str
    verified: bool
    id: str
    owner_id: str
    
    