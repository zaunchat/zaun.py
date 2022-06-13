import typing

if typing.TYPE_CHECKING:
    import schemas

class AdaptarProtocol(typing.Protocol):
    def __init__(self) -> None:
        super().__init__()
        
    def get_me(self) -> typing.Optional["schemas.User"]:
        raise NotImplementedError
    
    def get_user(
        self, 
        user_id: int
    ) -> typing.Optional["schemas.User"]:
        raise NotImplementedError
    
    def create_message(
        self, 
        content: str, 
        channel_id: int
    ) -> typing.Optional["schemas.Message"]:
        raise NotImplementedError
    
    def get_message(
        self, 
        id: int
    ) -> typing.Optional["schemas.Message"]:
        raise NotImplementedError
    
    def delete_message(
        self, 
        id: int
    ) -> None:
        raise NotImplementedError

    def edit_message(
        self, 
        id: int, 
        content: str
    ) -> typing.Optional["schemas.Message"]:
        raise NotImplementedError
    
    def register(
        self, 
        email: str, 
        password: str
    ) -> "schemas.User":
        raise NotImplementedError
    
    def verify_email(
        self, 
        id: int, 
        code: str
    ) -> None:
        raise NotImplementedError
    
    def sessions(self) -> typing.Optional[typing.List["schemas.Session"]]:
        raise NotImplementedError
    
    def create_session(
        self, 
        email: str, 
        password: str
    ) -> typing.Optional["schemas.Session"]:
        raise NotImplementedError
    
    def get_session(self, id: int) -> typing.Optional["schemas.Session"]:
        raise NotImplementedError
    
    def delete_session(self, id: int) -> None:
        raise NotImplementedError
    
    def get_channels(self) -> typing.Optional[typing.List["schemas.Channel"]]:
        raise NotImplementedError
    
    def create_channel(self, name: str) -> typing.Optional["schemas.Channel"]:
        raise NotImplementedError
    
    def join_channel(self, group_id: int, target_id: int) -> typing.Optional["schemas.Channel"]:
        raise NotImplementedError
    
    def get_channel(self, id: int) -> typing.Optional["schemas.Channel"]:
        raise NotImplementedError
    
    def delete_channel(self, id: int) -> None:
        raise NotImplementedError
    
    def create_server(self, name: str) -> typing.Optional["schemas.Server"]:
        raise NotImplementedError
    
    def get_server(self, id: int) -> typing.Optional["schemas.Server"]:
        raise NotImplementedError
    
    def delete_server(self, id: int) -> None:
        raise NotImplementedError
    
    def get_roles(self, server_id: int) -> typing.Optional[typing.List["schemas.Role"]]:
        raise NotImplementedError
    
    def create_role(
        self, 
        server_id: int, 
        name: str,
        color: int = 0, 
        hoist: bool = True, 
        permissions: int = 0
    ) -> typing.Optional["schemas.Role"]:
        raise NotImplementedError
    
    def get_role(self, server_id: int, role_id: int) -> typing.Optional["schemas.Role"]:
        raise NotImplementedError
    
    def delete_role(self, server_id: int, role_id: int) -> None:
        raise NotImplementedError
    
    def edit_role(
        self, 
        server_id: int,
        role_id: int,
        name: str ,
        color: int = 0, 
        hoist: bool = True, 
        permissions: int = 0
    ) -> typing.Optional["schemas.Role"]:
        raise NotImplementedError
        
    def get_members(self, server_id: int) -> typing.Optional[typing.List["schemas.Member"]]:
        raise NotImplementedError
    
    def get_member(self, server_id: int, user_id: int) -> typing.Optional["schemas.Member"]:
        raise NotImplemented
    
    def kick_member(self, server_id: int, user_id: int) -> None:
        raise NotImplemented
    
    def edit_member(self, server_id: int, user_id: int, roles: typing.List[int], nickname: str) -> typing.Optional["schemas.Member"]:
        raise NotImplementedError
    
    def create_channel(
        self, 
        server_id: int, 
        name: str, 
        type: "schemas.ChannelTypes"
    ) -> typing.Optional["schemas.Channel"]:
        raise NotImplementedError
    
    def delete_channel(
        self,
        server_id: int,
        channel_id: int
    ) -> None:
        raise NotImplementedError
    
    def edit_channel(
        self, 
        server_id: int,
        channel_id: int,
        name: str, 
        type: "schemas.ChannelTypes"
    ) -> typing.Optional["schemas.Channel"]:
        raise NotImplementedError
    
    def get_invites(
        self,
        server_id: int
    ) -> typing.Optional[typing.List["schemas.Invite"]]:
        raise NotImplementedError
    
    def create_invite(
        self,
        server_id: int,
    ) -> typing.Optional["schemas.Invite"]:
        raise NotImplementedError
    
    def get_invite(
        self,
        server_id: int,
        invite_id: int
    ) -> typing.Optional["schemas.Invite"]:
        raise NotImplementedError
    
    def delete_invite(
        self,
        server_id: int,
        invite_id: int
    ) -> None:
        raise NotImplementedError
    
    def get_bots(self) -> typing.Optional[typing.List["schemas.Bot"]]:
        raise NotImplementedError
    
    def create_bot(self) -> typing.Optional["schemas.Bot"]:
        raise NotImplementedError
    
    def get_bot(self, id: int) -> typing.Optional["schemas.Bot"]:
        raise NotImplementedError
    
    def delete_bot(self, id: int) -> None:
        raise NotImplementedError
    
    def create_invite(self, channel_id: int) -> typing.List["schemas.Invite"]:
        raise NotImplementedError
    
    def get_invite(self, code: str) -> typing.Optional["schemas.Invite"]:
        raise NotImplementedError
    
    def delete_invite(self, code: str) -> None:
        raise NotImplementedError
        
        
        
    
    