import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the channel delete event."
    
    channel = client.channels.get(payload["id"])
    "Get the channel to the cache."
    
    if channel:
        client.channels.cache.pop(channel.id)
    
    await client.emit(
        "on_channel_delete", channel)
    
def export():
    return "channelDelete", action