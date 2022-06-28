import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the user update event."
    
    user = client.users.add(payload)
    "Add the user to the cache."
    
    await client.emit(
        "on_user_update", user)
    
def export():
    return "userUpdate", action