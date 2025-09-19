import logging
import sys

def setup_logger():
    """
    Sets up a centralized logger for the test automation framework.
    """
    # Get the root logger
    logger = logging.getLogger("automation_tests")
    
    # Prevent duplicate handlers if this function is called multiple times
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # Create a handler to print log messages to the console (stdout)
    handler = logging.StreamHandler(sys.stdout)
    
    # Create a formatter to define the log message format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Set the formatter for the handler
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    # Prevent the logger from propagating messages to the root logger
    logger.propagate = False

    return logger

# Create a logger instance to be imported by other modules
log = setup_logger()