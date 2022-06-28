import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the server delete event."
    
    server = client.servers.get(payload['id'])
    "Add the server to the cache."
    
    await client.emit(
        "on_server_delete", server)
    
def export():
    return "serverDelete", action