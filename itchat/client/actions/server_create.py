import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the server create event."
    
    server = client.servers.add(payload)
    "Add the server to the cache."
    
    await client.emit(
        "on_server_create", server)
    
def export():
    return "serverCreate", action