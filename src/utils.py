from dataclasses import dataclass
import json
from typing import Any, Dict


@dataclass
class AWSEvent:
    httpMethod: str
    headers: Dict[str, str]
    body: Dict[str, Any]
    queryStringParameters: Dict[str, Any]
    pathParameters: Dict[str, Any]
    requestContext: Dict[str, Any]
    # Include more aws event types here

    def __init__(self, event) -> None:
        self.httpMethod = event.get("httpMethod", "")
        self.headers = event.get("headers", {})
        self.body = json.loads(event.get("body", "{}").encode("utf-8"))
        self.queryStringParameters = event.get("queryStringParameters", "")
        self.pathParameters = event.get("pathParameters", {})
        self.requestContext = event.get("requestContext", {})
        # Include more aws event types here


@dataclass
class Response:
    statusCode: int
    body: str
