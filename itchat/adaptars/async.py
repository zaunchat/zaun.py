import typing
import asyncio
import aiohttp
from itchat.errors.request_error import NotVaildRequest

if typing.TYPE_CHECKING:
    import schemas
   

import protocol
import routers
import errors
import rest

class ItChatAsync(protocol.AdaptarProtocol):
    """
    Async adaptar for ItChat API.
    """
    
    def __init__(
        self,
        rest: rest.RestOptions,
    ) -> None:
        
        self.rest: rest.RestOptions = rest
        "The rest options."
        
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()
        "The client session for the aiohttp."
        
    async def request(self, method: str, endpoint: str, json: typing.Dict = None) -> typing.Optional[typing.Dict]:
        """
        Make a request to the `:attr:rest.url`
        """
        
        kwargs = {}
        
        if json is not None:
            kwargs.update({
                'json': json
            })
        
        request = await self.session.request(
            method=method,
            url=self.rest.url + endpoint,
            **kwargs
        )
        
        if not request.ok:
            raise NotVaildRequest(f"Not vaild request for {endpoint}", request)
        
        return (await request.json())
        
        
    async def get_me(self) -> typing.Optional["schemas.User"]:
        return await self.request("GET", routers.GET_ME)
    
    async def get_user(self, user_id: int) -> typing.Optional["schemas.User"]:
        return await self.request("GET", routers.GET_USER)
    
    async def create_message(self, content: str, channel_id: int) -> typing.Optional["schemas.Message"]:
        return await self.request("POST", routers.CREATE_MESSAGES, {
            "content": content, "channel_id": channel_id
        })
    
    async def get_message(self, id: int) -> typing.Optional["schemas.Message"]:
        return await self.request("GET", routers.GET_MESSAGE, {
            "id": id
        })