from dataclasses import dataclass
from itchat.schemas import base

@dataclass
class Bot(base.APIObject):
    """
    The ratelimit class.
    """
    
    username: str
    verified: bool
    id: int
    owner_id: int
    
    