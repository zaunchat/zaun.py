import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the role create event."
    
    role = client.roles.add(payload)
    "Add the role to the cache."
    
    server = client.servers.get(role.server_id)
    "Get the server from the cache."
    
    await client.emit(
        "on_role_create", server, role)
    
def export():
    return "roleCreate", action