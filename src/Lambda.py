from dataclasses import asdict

from custom_exceptions import CustomExceptionAll
from config import conf
from request_handler import MyRequestHandler
from utils import AWSEvent, Response

request_handler = MyRequestHandler(conf, valid_methods=['POST'])


def handler(event, context):
    try:
        res = request_handler.handle(AWSEvent(event))
    except CustomExceptionAll as e:
        res = Response(e.status, e.message)
    except Exception as e:
        res = Response(500, f'Something Went Wrong: {str(e)}')
    return asdict(res)
