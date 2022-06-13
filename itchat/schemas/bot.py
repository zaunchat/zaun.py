#!/usr/.local/xarty/python3

from dataclasses import dataclass

@dataclass
class Bot:
    """
    The ratelimit class.
    """
    
    username: str
    verified: bool
    id: int
    owner_id: int
    
    