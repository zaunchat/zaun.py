import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the channel update event."
    
    new_channel = client.channels.add(payload)
    
    old_channel = client.channels.get(payload["id"])
    "Get the channel from the cache."
    
    await client.emit(
        "on_channel_update", old_channel, new_channel)
    
def export():
    return "ChannelUpdate", action