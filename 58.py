import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logging.info("This is an info message.")
    logging.error("This is an error message.")

# Example usage
setup_logging()
