from dataclasses import dataclass
from itchat.schemas import base

@dataclass
class RatelimitInfo(base.APIObject):
    """
    The ratelimit class.
    """
    
    __slots__ = 'remaining', 'retry_after', 'limit'
    
    remaining: int
    retry_after: int
    limit: int