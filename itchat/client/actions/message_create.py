import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the message create event."
    
    message = client.messages.add(payload)
    "Add the channel to the cache."
    
    await client.emit(
        "on_message_create", message)
    
def export():
    return "messageCreate", action