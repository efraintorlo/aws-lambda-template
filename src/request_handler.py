import json
from typing import List

from authorizer import JWTAuthorizer
from config import Config
from custom_exceptions import BadRequest
from request_handler_base import RequestHandlerBase
from utils import AWSEvent, Response


class MyRequestHandler(RequestHandlerBase):
    def __init__(self, conf: Config, valid_methods: List[str]) -> None:
        super().__init__(conf=conf, authorizer=JWTAuthorizer(conf), valid_methods=valid_methods)

    def post(self, event: AWSEvent) -> Response:
        jwt_payload = self.auth(event)
        if self.conf.VERBOSE:
            print(jwt_payload)
            print(event)

        if not event.body:
            raise BadRequest("Body Not Found")

        # INCLUDE HERE BUSINESS LOGIC
        # service = Myservice(conf)
        # res = service.do_stuff(event.body)
        res = {"message": "cool"}
        return Response(200, json.dumps(res))
