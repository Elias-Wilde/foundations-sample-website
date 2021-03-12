import logging
from logging.handlers import RotatingFileHandler


def setup_logger(debug):
    MAX_BYTES = 10000000  # Maximum size for a log file
    BACKUP_COUNT = 9  # Maximum number of old log files
    LOG_LEVEL = logging.INFO

    if debug:
        LOG_LEVEL = logging.DEBUG

    # get root logger
    logger = logging.getLogger()
    # the level should be the lowest level set in handlers
    logger.setLevel(LOG_LEVEL)

    log_format = logging.Formatter('[%(levelname)s] %(asctime)s [%(name)s] - %(message)s')

    # stream handler - logs everything with log level LOG_LEVEL and above to termianl (stdout)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_format)
    stream_handler.setLevel(LOG_LEVEL)
    logger.addHandler(stream_handler)

    # rotating file handler 1 - logs everything with log level INFO and above to 'logs/log.txt'
    info_handler = RotatingFileHandler(
        'logs/log.txt', maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
    info_handler.setFormatter(log_format)
    info_handler.setLevel(logging.INFO)
    logger.addHandler(info_handler)

    # rotating file handler 2 - logs everything with log level ERROR and above to 'logs/error.txt'
    error_handler = RotatingFileHandler(
        'logs/error.txt', maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
    error_handler.setFormatter(log_format)
    error_handler.setLevel(logging.ERROR)
    logger.addHandler(error_handler)
