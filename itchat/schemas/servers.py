from dataclasses import dataclass
from typing import List

from itchat.schemas import base

@dataclass
class Server(base.APIObject):
    """
    The server class.
    """
    
    __slots__ = 'id', 'name', 'owner_id', 'permissions', 'icon', 'description', 'banner'
    
    id: str
    name: str
    owner_id: str
    permissions: int
    icon: str
    description: str
    banner: str
    
@dataclass
class Role:
    """
    The role class.
    """
    
    __slots__ = 'id', 'name', 'hoist', 'color', 'permissions', 'server_id'
    
    id: str
    name: str
    hoist: str
    color: int
    permissions: int
    server_id: str
    
@dataclass
class Member:
    """
    The member class.
    """
    
    __slots__ = 'id', 'roles', 'nickname', 'joined_at', 'server_id'
    
    id: str
    roles: List[int]
    nickname: str
    joined_at: str
    server_id: str
    
@dataclass
class Invite:
    """
    The invite class.
    """
    
    __slots__ = 'channel_id', 'server_id', 'id', 'code', 'invter_id', 'uses'
    
    channel_id: str
    server_id: str
    id: str
    code: str
    inviter_id: str
    uses: int