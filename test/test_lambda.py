
import os
import sys

from pytest import fixture

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(THIS_DIR, '..', 'src'))

from Lambda import handler


@fixture
def aws_event() -> dict:
    return {'httpMethod': 'POST', 'headers': {'Authorization': 'Bearer 1234'}}

@fixture
def aws_context() -> dict:
    return {'function_name': 'test-function'}


def test_post_is_valid(aws_event, aws_context):
    res = handler(aws_event, aws_context)
    assert res['statusCode'] != 405

def test_post_is_authenticated(aws_event, aws_context):
    res = handler(aws_event, aws_context)
    assert res['statusCode'] == 401