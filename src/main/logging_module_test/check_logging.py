import logging


def get_logger():

    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Set the logger level

    # Create a stream handler (console)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Set the handler level

    # Create a formatter and attach it to the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add the handler to the logger (avoid duplicates)
    if not logger.hasHandlers():
        logger.addHandler(console_handler)

    return logger

