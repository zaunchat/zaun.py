from dataclasses import dataclass
from itchat.schemas import base
@dataclass
class User(base.APIObject):
    """
    The user class.
    """
    
    __slots__ = 'id', 'username', 'badges', 'password', 'email', 'avatar', 'verified', 'relationship'
    
    id: str
    username: str
    badges: int
    password: str
    email: str
    avatar: str
    verified: bool
    relationship: str