import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the role update event."
    
    new_role = client.roles.add(payload)
    "Add the role to the cache."
    
    old_role = client.roles.get(new_role.id)
    "Get the role from the cache."
    
    server = client.servers.get(new_role.server_id)
    "Get the server from the cache."
    
    await client.emit(
        "on_role_update", server, old_role, new_role)
    
def export():
    return "RoleUpdate", action