from abc import ABC, abstractmethod
from typing import Any, Dict

import jwt

from config import Config
from utils import AWSEvent


class Authorizer(ABC):

    @abstractmethod
    def create_token(self, identity: str) -> str:
        pass

    @abstractmethod
    def authorize(self, aws_event: AWSEvent) -> Dict[str, Any]:
        pass


class JWTAuthorizer(Authorizer):
    def __init__(self, conf: Config) -> None:
        self.conf = conf

    def create_token(self, identity: str) -> str:
        return jwt.encode(
            {
                "aud": self.conf.JWT_AUDIENCE,
                "sub": identity,
                "exp": self.conf.JWT_EXPIRATION_TIME,
            },
            self.conf.JWT_SECRET_KEY,
            algorithm=self.conf.JWT_ALGORITHM,
        ).decode("utf-8")

    def authorize(self, aws_event: AWSEvent) -> Dict[str, Any]:
        _, token = aws_event.headers["Authorization"].split(" ")
        payload = jwt.decode(
            token,
            self.conf.JWT_SECRET_KEY,
            audience=self.conf.JWT_AUDIENCE,
            algorithms=self.conf.JWT_ALGORITHM,
        )
        return payload