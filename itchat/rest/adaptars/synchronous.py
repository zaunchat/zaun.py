import typing
import threading
import requests
import logging

log = logging.getLogger('itchat.rest')

from itchat.rest import rest, protocol

class SyncREST(protocol.AdaptarProtocol):
    
    """
    A sync adaptar for ItChat which implements the ItChat ratelimit.
    It's built on top of requests library, using threading.Lock to prevent
    other threads from accessing the session at the same time.
    """
    
    def __init__(
        self,
        rest: rest.RestOptions,
        *,
        max_retries: int = 3,
        retry_delay: float = 1.0,
    ) -> None:
        
        self.rest = rest
        "The rest options."
        
        self.session = requests.Session()
        "The requests session."
        
        self.lock = threading.Lock()
        "The lock for the session."
        
        self.max_retries = max_retries
        "The max retries for the itchat API."
        
        self.retry_delay = retry_delay
        "The retry delay for the itchat API."
        
        # Rest ratelimit
        
        self.bucket: typing.Dict[str, int] = {}
        
    def set_token(self, token: str) -> None:
        """
        Set the token for the adaptar.
        """
        #TODO: implement a way to validate the token.
        
        self.rest.headers["Authorization"] = token
        
    def request(self, method: str, endpoint: str, **options: typing.Any) -> typing.Dict:
        """Make a request to the `:attr:endpoint`
        And retrieve the data and parse into a dict,
        it handles the error and ratelimit of the itchat API.
        
        Async implementation.

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
        #TODO: implement a ratelimit handler.
        
        self.lock.acquire()
        
        if endpoint not in self.bucket:
            self.bucket[endpoint] = 0
        
        res = self.session.request(
            method=method, url=endpoint, **options)
        
        if res.ok:
            if res.headers.get('Content-Type') == 'application/json':
                return res.json()
            return res.text
        
        if res.status == 429:
            log.debug("Ratelimit reached, waiting for %s seconds.", self.retry_delay)
            
        if res.status >= 500 and res.status < 600:
            if self.bucket[endpoint] >= self.max_retries:
                log.error("Max retries reached, aborting.")
                
                return self.request(method, endpoint, **options)
            
        self.lock.release()