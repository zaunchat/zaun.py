GET_ME = "/users/@me"
GET_USER = "/users/{}"

CREATE_MESSAGES = "/messages"
GET_MESSAGE = "/messages/{}"
DELETE_MESSAGE = "/messages/{}"
EDIT_MESSAGE = "/messages/{}"

ACCOUNTS = "/auth/accounts/register"
GET_VERFIY_CODE = "/auth/accounts/verify/{}/{}"

GET_AUTH_SESSIONs = "/auth/session"
CREATE_AUTH_SESSIONs = "/auth/session"

GET_AUTH_SESSION = "/auth/sessions/{}"
DELETE_AUTH_SESSION = "/auth/sessions/{}"

GET_GROUP = "/channels"
CREATE_GROUP = "/channels"
JOIN_GROUP = "/channels/join/{}/{}"

GET_CHANNEL = "/channels/{}"
DELETE_CHANNEL = "/channels/{}"

CREATE_SERVER = "/servers"
GET_SERVER = "/servers/{}"
DELETE_SERVER = "/servers/{}"

GET_SERVERS = "/servers"

GET_ROLES = "/servers/{}/roles"

CREATE_ROLE = "/servers/{}/roles"
GET_ROLE = "/servers/{}/roles/{}"
DELETE_ROLE = "/servers/{}/roles/{}"
EDIT_ROLE = "/servers/{}/roles/{}"

GET_MEMBERS = "/servers/{}/members"
GET_MEBMER = "/servers/{}/mebmers/{}"
DELETE_MEMBER = "/servers/{}/mebmers/{}"
EDIT_MEMBER = "/servers/{}/mebmers/{}"

CREATE_CHANNEL = "/servers/{}/channels"
DELETE_CHANNEL = "/servers/{}/channels/{}"
EDIT_CHANNEL = "/servers/{}/channels/{}"

GET_SERVER_INVITES = "/servers/{}/invites"
CREATE_SERVER_INVITE = "/servers/{}/invites"

GET_SERVER_INVITE = "/servers/{}/invites/{}"
DELETE_SERVER_INVITE = "/servers/{}/invites/{}"

GET_BOTS = "/bots"
CREATE_BOT = "/bots"

GET_BOT = "/bots/{}"
DELETE_BOT = "/bots/{}"

#CREATE_INVITE = "/invites"
GET_INVITE = "/invites/{}"
CREATE_INVITE = "/invites"