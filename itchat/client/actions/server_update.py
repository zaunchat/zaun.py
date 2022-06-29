import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the server update event."
    
    new_server = client.servers.add(payload)
    "Add the server to the cache."
    
    old_server = client.servers.get(new_server.id)
    "Get the server from the cache."
    
    await client.emit(
        "on_server_update", old_server, new_server)
    
def export():
    return "ServerUpdate", action