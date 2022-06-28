import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: a handler for the ready event."
        
    shard.last_pong_acked = True
    
    for user in payload['users']:
        client.users.add(user)
    
    for server in payload['servers']:
        client.servers.add(server)
        
    for channel in payload['channels']:
        client.channels.add(channel)
        
    # TODO: implement heartbeat
        
    shard.is_ready = True
    
def export():
    return "ready", action