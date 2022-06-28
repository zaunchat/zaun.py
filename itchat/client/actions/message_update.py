import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the message update event."
    
    new_message = client.messages.add(payload)
    "Add the message to the cache."
    
    old_message = client.messages.get(new_message.id)
    "Get the message from the cache."
    
    await client.emit(
        "on_message_update", old_message, new_message)
    
def export():
    return "messageUpdate", action