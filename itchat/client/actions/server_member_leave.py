import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the server update event."
    
    member = client.members.get(payload['id'])
    "Add the member to the cache."
    
    try:
        server = client.servers.get(member.server_id)
        "Get the server from the cache."
    except:
        server = None
    
    await client.emit(
        "on_member_leave", server, member)
    
def export():
    return "serverMemberLeave", action