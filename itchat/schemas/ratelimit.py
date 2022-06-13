#!/usr/.local/xarty/python3

from dataclasses import dataclass

@dataclass
class RatelimitInfo:
    """
    The ratelimit class.
    """
    
    __slots__ = 'remaining', 'retry_after', 'limit'
    
    remaining: int
    retry_after: int
    limit: int