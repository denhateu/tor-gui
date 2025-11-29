import logging
from datetime import datetime


def setup_logging():
    logger = logging.getLogger("mylogger")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Avoid adding handler twice
    if not logger.handlers:
        # Gets now date and time for logs file name
        now = datetime.now()
        now_time = now.strftime("%Y-%m-%d %H_%M_%S")

        logs_file_name = f"app_logs {now_time}.log"

        console_handler = logging.StreamHandler()
        log_file_handler = logging.FileHandler(logs_file_name)

        formatter = logging.Formatter(
            "[ %(levelname)s ] %(asctime)s - %(message)s"
        )

        console_handler.setFormatter(formatter)
        log_file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(log_file_handler)

    logger.info(f"Starting logs writing at {now_time}")

    return logger
