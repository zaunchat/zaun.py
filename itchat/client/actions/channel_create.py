import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the channel create event."
    
    channel = client.channels.add(payload)
    "Add the channel to the cache."
    
    await client.emit(
        "on_channel_create", channel)
    
def export():
    return "channelCreate", action