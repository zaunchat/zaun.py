import typing

if typing.TYPE_CHECKING:
    import schemas

class AdaptarProtocol(typing.Protocol):
    """
    A protocol for ItChat which implements the methods of the protocol.AdaptarProtocol.
    """

    def request(self, method: str, endpoint: str, **options: typing.Any) -> typing.Dict:
        """Make a request to the `:attr:endpoint`
        And retrieve the data and parse into a dict,
        it handles the error and ratelimit of the itchat API.
        
        Adaptar implementation is a way to make async and sync code
        easier to use. It is a bridge between the sync and async code.

        Arguments:
        --------
        method: str
            The method of the request.
        endpoint: str
            The endpoint of the request.
        headers: typing.Optional[typing.Dict]
            the headers of the request.
        params: typing.Optional[typing.Dict]
            the params of the request.
        **options: typing.Any
            the options of the request.
        """
        raise NotImplementedError
    
    def post(self, endpoint: str, **options: typing.Any) -> typing.Any:
        "An alias for :meth:`request`."
        raise NotImplementedError
    
    def get(self, endpoint: str, **options: typing.Any) -> typing.Any:
        "An alias for :meth:`request`."
        raise NotImplementedError
    
    def patch(self, endpoint: str, **options: typing.Any) -> typing.Any:
        "An alias for :meth:`request`."
        raise NotImplementedError
    
    def delete(self, endpoint: str, **options: typing.Any) -> typing.Any:
        "An alias for :meth:`request`."
        raise NotImplementedError
    
    def put(self, endpoint: str, **options: typing.Any) -> typing.Any:
        "An alias for :meth:`request`."
        raise NotImplementedError