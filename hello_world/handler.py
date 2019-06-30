import json
import os
import logging

from greet import greet


log_format = '[%(asctime)s - %(name)s - %(filename)s: %(lineno)d \
    - %(levelname)s] - %(message)s'

logging.basicConfig(
    format=log_format,
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def hello(event, context):
    logger.info('Running from inside function.')
    print("the env variable is: ", os.getenv('SOME_VAR'))
    body = {
        "message": greet(),
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    logger.info(response)

    return response


if __name__ == "__main__":

    logger = logging.getLogger(__name__)
    # logger.info('Running function...')
    logger.info(hello("", ""))
    # logger.info('Done.')