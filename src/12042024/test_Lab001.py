import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("This is information logs")
    LOGGER.warning("This is warning logs")
    LOGGER.error("This is error logs")
    LOGGER.critical("This is Critical logs")
