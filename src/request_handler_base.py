from typing import Any, Dict, List

from authorizer import Authorizer
from custom_exceptions import AuthError, MethodNotAllowed
from config import Config
from utils import AWSEvent, Response


class RequestHandlerBase:
    def __init__(
        self,
        conf: Config,
        authorizer: Authorizer,
        valid_methods: List[str] = ["POST", "GET"],
    ) -> None:
        self.conf = conf
        self.authorizer = authorizer
        self.valid_methods = valid_methods

    def auth(self, event: AWSEvent) -> Dict[str, Any]:
        try:  # Auth is delagated to the authorizer
            return self.authorizer.authorize(event)
        except Exception as e:
            raise AuthError(str(e))

    def handle(self, event: AWSEvent) -> Response:
        method = event.httpMethod
        if method not in self.valid_methods:
            raise MethodNotAllowed()
        if method == "POST":
            return self.post(event)
        elif method == "GET":
            return self.get(event)

    def get(self, event: AWSEvent) -> Response:
        raise NotImplementedError

    def post(self, event: AWSEvent) -> Response:
        raise NotImplementedError
