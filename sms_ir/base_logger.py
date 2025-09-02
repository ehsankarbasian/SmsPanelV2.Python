import sys
import logging


def get_default_logger():
    # setup logging
    log_level = logging.INFO

    log_format = logging.Formatter("[%(asctime)s] [%(levelname)s] - %(message)s")
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # writing to stdout
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(log_level)
    handler.setFormatter(log_format)
    logger.addHandler(handler)
    
    return logger
