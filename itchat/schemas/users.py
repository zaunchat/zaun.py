#!/usr/.local/xarty/python3

from dataclasses import dataclass

@dataclass
class User:
    """
    The user class.
    """
    
    __slots__ = 'id', 'username', 'badges', 'password', 'email', 'avatar'
    
    id: int
    username: str
    badges: int
    password: str
    email: str
    avatar: str