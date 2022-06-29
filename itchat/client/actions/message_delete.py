import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the message delete event."
    
    message = client.messages.get(payload["id"])
    "Get the message to the cache."
    
    if message:
        client.messages.cache.pop(message.id)
        
    await client.emit(
        "on_message_delete", message)
    
def export():
    return "MessageDelete", action