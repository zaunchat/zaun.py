import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the role delete event."
    
    role = client.roles.get(payload["id"])
    "Get the role to the cache."
    
    if role:
        client.roles.cache.pop(role.id)
        
    try:
        server = client.servers.get(role.server_id)
        "Get the server from the cache."
    except:
        server = None
    
    await client.emit(
        "on_role_delete", server, role)
    
def export():
    return "RoleDelete", action