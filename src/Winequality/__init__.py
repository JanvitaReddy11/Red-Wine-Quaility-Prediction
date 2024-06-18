# Example __init__.py in src/Winequality/logging/__init__.py

import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s:%(module)s:%(message)s]"

# Assuming log_dir and log_filepath are defined correctly in your setup

log_dir = "logs"
log_filepath = "logs/running_log.log"

# Ensure the log directory exists
import os
os.makedirs(log_dir, exist_ok=True)

# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # File handler to save logs to a file
        logging.StreamHandler(sys.stdout)  # Stream handler to print logs to console
    ]
)

# Logger instance
logger = logging.getLogger("Winequality logger")
