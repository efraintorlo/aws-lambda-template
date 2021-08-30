import os
from dataclasses import dataclass

ENVIRONMENT = os.getenv('ENVIRONMENT', 'Development')

@dataclass
class Config:
    VERBOSE: bool = True
    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY', 'my-secret-key')
    JWT_AUDIENCE: str = os.getenv('JWT_AUDIENCE', 'my-audience')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM', 'HS256')
    JWT_EXPIRATION_TIME: int = int(os.getenv('JWT_EXPIRATION_TIME', '3600'))
    ES_USER: str = os.getenv('ES_USER', 'test')
    ES_PASSWORD: str = os.getenv('ES_PASSWORD', 'test')
    # Add credentials to be used 


@dataclass
class DevelopmentConfig(Config):
    pass


@dataclass
class ProductionConfig(Config):
    VERBOSE = False


if ENVIRONMENT == 'Development':
    conf = DevelopmentConfig()
elif ENVIRONMENT == 'Production':
    conf = ProductionConfig()
else: 
    conf = Config()