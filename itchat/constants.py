import enum

class WSEvents(enum.Enum):
  	AUTHENTICATE = 'Authenticate'
  	AUTHENTICATED = 'Authenticated'
  	CHANNEL_CREATE = 'ChannelCreate'
  	CHANNEL_DELETE = 'ChannelDelete'
  	CHANNEL_UPDATE = 'ChannelUpdate'
  	ERROR = 'Error'
  	MESSAGE_CREATE = 'Message'
  	MESSAGE_DELETE = 'MessageDelete'
  	MESSAGE_UPDATE = 'MessageUpdate'
  	PING = 'Ping'
  	PONG = 'Pong'
  	READY = 'Ready'
  	SERVER_CREATE = 'ServerCreate'
  	SERVER_DELETE = 'ServerDelete'
  	SERVER_MEMBER_JOIN = 'ServerMemberJoin'
  	SERVER_MEMBER_LEAVE = 'ServerMemberLeave'
  	SERVER_MEMBER_UPDATE = 'ServerMemberUpdate'
  	SERVER_ROLE_CREATE = 'RoleCreate'
  	SERVER_ROLE_DELETE = 'RoleDelete'
  	SERVER_ROLE_UPDATE = 'RoleUpdate'
  	SERVER_UPDATE = 'ServerUpdate'
  	USER_UPDATE = 'UserUpdate'


class Events(enum.Enum):
  	CHANNEL_CREATE = 'channelCreate'
  	CHANNEL_DELETE = 'channelDelete'
  	CHANNEL_UPDATE = 'channelUpdate'
  	MESSAGE_CREATE = 'messageCreate'
  	MESSAGE_DELETE = 'messageDelete'
  	MESSAGE_UPDATE = 'messageUpdate'
  	RAW = 'raw'
  	READY = 'ready'
  	ROLE_CREATE = 'roleCreate'
  	ROLE_DELETE = 'roleDelete'
  	ROLE_UPDATE = 'roleUpdate'
  	SERVER_CREATE = 'serverCreate'
  	SERVER_DELETE = 'serverDelete'
  	SERVER_UPDATE = 'serverUpdate'
  	SERVER_MEMBER_JOIN = 'serverMemberJoin'
  	SERVER_MEMBER_LEAVE = 'serverMemberLeave'
  	SERVER_MEMBER_UPDATE = 'serverMemberUpdate'
  	USER_UPDATE = 'userUpdate'

default_client_options = {
  "ws_url": "wss://api.itchat.world/ws",
  "ws_heartbeat_interval": 0,
  "ws_reconnect": 0,
  
  "rest_api_url": "https://api.itchat.world",
  "rest_app": "https://app.itchat.world",
  "cdn_url": "https://cdn.itchat.world",
  "rest_timeout": 10,
  "retries": 3,
}