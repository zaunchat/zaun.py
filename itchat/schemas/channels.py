from dataclasses import dataclass
from enum import Enum
from typing import List

from itchat.schemas import base

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
class Overwrite(base.APIObject):
    """
    Overwrite class.
    """
    
    __slots__ = 'type', 'allow','deny', 'id'
    
    type: int
    allow: int
    deny: int
    id: int
    
@dataclass
class Channel(base.APIObject):
    """
    The channel class.
    """
    
    __slots__ = 'id','topic', 'name', 'parent_id', 'recipients', 'type', 'server_id', 'owner_id', 'permissions', 'overwrites'
    
    id: int
    topic: str
    name: str
    parent_id: int
    recipients: List[int]
    type: ChannelTypes
    server_id: int
    owner_id: int
    permissions: int
    overwrites: List[Overwrite]
    

    