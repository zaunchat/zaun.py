#!/usr/.local/xarty/python3

from dataclasses import dataclass

@dataclass
class Message:
    """
    The message class.
    """
    
    __slots__ = 'id', 'content', 'author_id', 'edited_at', 'channel_id'
    
    id: int
    content: str
    author_id: int
    edited_at: int
    channel_id: int