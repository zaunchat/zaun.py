import typing

if typing.TYPE_CHECKING:
    from itchat.client import Client, WebSocketShard
    
async def action(
    client: "Client",
    shard: "WebSocketShard",
    payload: dict,
) -> None:
    "Coro: The handler for the members update event."
    
    new_member = client.members.add(payload)
    "Add the member to the cache."
    
    old_member = client.roles.get(new_member.id)
    "Get the member from the cache."
    
    server = client.servers.get(new_member.server_id)
    "Get the server from the cache."
    
    await client.emit(
        "on_member_update", server, old_member, new_member)
    
def export():
    return "ServerMemberUpdate", action