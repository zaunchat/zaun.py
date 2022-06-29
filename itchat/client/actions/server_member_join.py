import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the server update event."
    
    member = client.members.add(payload)
    "Add the member to the cache."
    
    server = client.servers.get(member.server_id)
    "Get the server from the cache."
    
    await client.emit(
        "on_member_join", server, member)
    
def export():
    return "ServerMemberJoin", action