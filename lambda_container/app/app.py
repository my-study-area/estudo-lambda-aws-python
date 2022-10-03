import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def handler(event, context):
    logging.info('Lambda container')
    return {
        "message": "I'm inside the container"
    }
