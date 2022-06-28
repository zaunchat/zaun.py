from dataclasses import dataclass
from itchat.schemas import base
@dataclass
class Session(base.APIObject):
    """
    The session class.
    """
    
    __slots__ = 'token', 'id', 'user_id'
    
    token: str
    id: str
    user_id: int
    
