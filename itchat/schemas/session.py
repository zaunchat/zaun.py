#!/usr/.local/xarty/python3

from dataclasses import dataclass

@dataclass
class Session:
    """
    The session class.
    """
    
    __slots__ = 'token', 'id', 'user_id'
    
    token: str
    id: int
    user_id: int
    
