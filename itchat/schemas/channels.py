#!/usr/.local/xarty/python3

from dataclasses import dataclass
from enum import Enum
from typing import List

class ChannelTypes(Enum):
    """
    Enum for channel types.
    """
    DIRECT = "DIRECT"
    GROUP = "GROUP"
    TEXT = "TEXT"
    VOICE = "VOICE"
    CATEGORY = "CATEGORY"
    UNKNOWN = "UNKNOWN"
    
class OverwriteTypes(Enum):
    """
    Enum for overwrite types.
    """
    
    ROLE = "role"
    MEMBER = "member"
    
@dataclass
class Overwrite:
    """
    Overwrite class.
    """
    
    __slots__ = 'type', 'allow','deny', 'id'
    
    type: int
    allow: int
    deny: int
    id: int
    
@dataclass
class Channel:
    """
    The channel class.
    """
    
    __slots__ = 'topic', 'name', 'parent_id', 'recipients', 'type', 'server_id', 'owner_id', 'permissions', 'overwrites'
    
    topic: str
    name: str
    parent_id: int
    recipients: List[int]
    type: ChannelTypes
    server_id: int
    owner_id: int
    permissions: int
    overwrites: List[Overwrite]
    

    