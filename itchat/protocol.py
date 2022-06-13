import typing

if typing.TYPE_CHECKING:
    import schemas

class AdaptarProtocol(typing.Protocol):
    def __init__(self) -> None:
        super().__init__()

    def get_me(self) -> typing.Optional["schemas.User"]:
        """
        Get the user that is currently logged in.
        """
        raise NotImplementedError

    def get_user(self, user_id: int) -> typing.Optional["schemas.User"]:
        """
        Get user by id.
        """
        raise NotImplementedError

    def create_message(
        self, content: str, channel_id: int
    ) -> typing.Optional["schemas.Message"]:
        """
        Create a message.
        """

        raise NotImplementedError

    def get_message(self, id: int) -> typing.Optional["schemas.Message"]:
        """
        Get message by id.
        """

        raise NotImplementedError

    def delete_message(self, id: int) -> None:
        """
        Delete a message.
        """

        raise NotImplementedError

    def edit_message(self, id: int, content: str) -> typing.Optional["schemas.Message"]:
        """
        Edit a message.
        """

        raise NotImplementedError

    def register(self, email: str, password: str) -> "schemas.User":
        """
        Register a new user.
        """

        raise NotImplementedError

    def verify_email(self, id: int, code: str) -> None:
        """
        Verify an email address.
        """

        raise NotImplementedError

    def sessions(self) -> typing.Optional[typing.List["schemas.Session"]]:
        """
        Get all sessions.
        """

        raise NotImplementedError

    def create_session(
        self, email: str, password: str
    ) -> typing.Optional["schemas.Session"]:
        """
        Create a session.
        """

        raise NotImplementedError

    def get_session(self, id: int) -> typing.Optional["schemas.Session"]:
        """
        Get session by id.
        """
        raise NotImplementedError

    def delete_session(self, id: int) -> None:
        """
        Delete a session.
        """
        raise NotImplementedError

    def get_channels(self) -> typing.Optional[typing.List["schemas.Channel"]]:
        """
        Get all channels.
        """
        raise NotImplementedError

    def create_channel(self, name: str) -> typing.Optional["schemas.Channel"]:
        """
        Create a channel.
        """

        raise NotImplementedError

    def join_channel(
        self, group_id: int, target_id: int
    ) -> typing.Optional["schemas.Channel"]:
        """
        Join a channel.
        """

        raise NotImplementedError

    def get_channel(self, id: int) -> typing.Optional["schemas.Channel"]:
        """
        Get channel by id.
        """

        raise NotImplementedError

    def delete_channel(self, id: int) -> None:
        """
        Delete a channel.
        """

        raise NotImplementedError

    def create_server(self, name: str) -> typing.Optional["schemas.Server"]:
        """
        Create a server.
        """

        raise NotImplementedError

    def get_server(self, id: int) -> typing.Optional["schemas.Server"]:
        """
        Get server by id.
        """

        raise NotImplementedError

    def delete_server(self, id: int) -> None:
        """
        Delete a server.
        """
        raise NotImplementedError

    def get_roles(self, server_id: int) -> typing.Optional[typing.List["schemas.Role"]]:
        """
        Get roles.
        """

        raise NotImplementedError

    def create_role(
        self,
        server_id: int,
        name: str,
        color: int = 0,
        hoist: bool = True,
        permissions: int = 0,
    ) -> typing.Optional["schemas.Role"]:
        """
        Create a role.
        """

        raise NotImplementedError

    def get_role(self, server_id: int, role_id: int) -> typing.Optional["schemas.Role"]:
        """
        Get role by id.
        """

        raise NotImplementedError

    def delete_role(self, server_id: int, role_id: int) -> None:
        """
        Delete a server role.
        """

        raise NotImplementedError

    def edit_role(
        self,
        server_id: int,
        role_id: int,
        name: str,
        color: int = 0,
        hoist: bool = True,
        permissions: int = 0,
    ) -> typing.Optional["schemas.Role"]:
        """
        Edit a role.
        """

        raise NotImplementedError

    def get_members(
        self, server_id: int
    ) -> typing.Optional[typing.List["schemas.Member"]]:
        """
        Get members.
        """

        raise NotImplementedError

    def get_member(
        self, server_id: int, user_id: int
    ) -> typing.Optional["schemas.Member"]:
        """
        Get member by id.
        """

        raise NotImplemented

    def kick_member(self, server_id: int, user_id: int) -> None:
        """
        Kick a member.
        """

        raise NotImplemented

    def edit_member(
        self, server_id: int, user_id: int, roles: typing.List[int], nickname: str
    ) -> typing.Optional["schemas.Member"]:
        """
        Edit a member.
        """

        raise NotImplementedError

    def create_channel(
        self, server_id: int, name: str, type: "schemas.ChannelTypes"
    ) -> typing.Optional["schemas.Channel"]:
        """
        Create a channel.
        """

        raise NotImplementedError

    def delete_channel(self, server_id: int, channel_id: int) -> None:
        """
        Delete a channel.
        """

        raise NotImplementedError

    def edit_channel(
        self, server_id: int, channel_id: int, name: str, type: "schemas.ChannelTypes"
    ) -> typing.Optional["schemas.Channel"]:
        """
        Edit a channel.
        """

        raise NotImplementedError

    def get_invites(
        self, server_id: int
    ) -> typing.Optional[typing.List["schemas.Invite"]]:
        """
        Get invites.
        """

        raise NotImplementedError

    def create_invite(
        self,
        server_id: int,
    ) -> typing.Optional["schemas.Invite"]:
        """
        Create an invite.
        """

        raise NotImplementedError

    def get_invite(
        self, server_id: int, invite_id: int
    ) -> typing.Optional["schemas.Invite"]:
        """
        Get invite by id.
        """

        raise NotImplementedError

    def delete_invite(self, server_id: int, invite_id: int) -> None:
        """
        Delete an invite by id.
        """

        raise NotImplementedError

    def get_bots(self) -> typing.Optional[typing.List["schemas.Bot"]]:
        """
        Get bots.
        """

        raise NotImplementedError

    def create_bot(self) -> typing.Optional["schemas.Bot"]:
        """
        Create a bot.
        """
        raise NotImplementedError

    def get_bot(self, id: int) -> typing.Optional["schemas.Bot"]:
        """
        Get bot by id.
        """

        raise NotImplementedError

    def delete_bot(self, id: int) -> None:
        """
        Delete a bot.
        """

        raise NotImplementedError

    def create_invite(self, channel_id: int) -> typing.List["schemas.Invite"]:
        """
        Create an invite.
        """
        raise NotImplementedError

    def get_invite(self, code: str) -> typing.Optional["schemas.Invite"]:
        """
        Get invite by code.
        """

        raise NotImplementedError

    def delete_invite(self, code: str) -> None:
        """
        Delete an invite by code.
        """
        raise NotImplementedError
