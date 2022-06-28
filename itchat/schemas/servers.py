from dataclasses import dataclass
from typing import List

@dataclass
class Server:
    """
    The server class.
    """
    
    __slots__ = 'id', 'name', 'owner_id', 'permissions', 'icon', 'description', 'banner'
    
    id: int
    name: str
    owner_id: int
    permissions: int
    icon: str
    description: str
    banner: str
    
@dataclass
class Role:
    """
    The role class.
    """
    
    __slots__ = 'name', 'hoist', 'color', 'permissions', 'server_id'
    
    name: str
    hoist: str
    id: int
    color: int
    permissions: int
    server_id: int
    
@dataclass
class Member:
    """
    The member class.
    """
    
    __slots__ = 'id', 'roles', 'nickname', 'joined_at', 'server_id'
    
    id: int
    roles: List[int]
    nickname: str
    joined_at: str
    server_id: int
    
@dataclass
class Invite:
    """
    The invite class.
    """
    
    __slots__ = 'channel_id', 'server_id', 'id', 'code', 'invter_id', 'uses'
    
    channel_id: int
    server_id: int
    id: int
    code: str
    inviter_id: int
    uses: int