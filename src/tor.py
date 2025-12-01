import os
import subprocess
import threading
import logging
from datetime import datetime

from ui.logs_page import append_logs


# Setup logging
logger = logging.getLogger("mylogger")


class Tor:
    def __init__(self) -> None:
        self.tor_path = "tor\\tor\\tor.exe"
        self.tor_config_path = "tor\\tor\\torrc"

        # Gets now date and time for logs file name
        now = datetime.now()
        now_time = now.strftime("%Y-%m-%d %H_%M_%S")

        logs_file_name = f"tor_logs {now_time}.log"
        self.tor_logs_file_path = f"tor\\logs\\{logs_file_name}"

        # Create logs directory if not exists
        if not os.path.exists("tor\\logs"):
            os.mkdir("tor\\logs")

        self.default_config = """
SocksPort localhost:9050
HTTPTunnelPort localhost:8118
"""

        self.tor_thread = None
        self.tor_process = None

    def config_exists(self) -> bool:
        global logger

        if os.path.exists(self.tor_config_path):
            logger.info(f"{self.tor_config_path} config found")
            return True
        else:
            logger.warning(f"{self.tor_config_path} config not found!")
            return False

    def create_default_config(self) -> None:
        global logger

        with open(self.tor_config_path, "w", encoding="utf-8") as config_file:
            config_file.write(self.default_config)

        logger.info(f"Created default {self.tor_config_path} config")

    def get_config(self):
        with open(self.tor_config_path, "r", encoding="utf-8") as config_file:
            config = config_file.read()

        return config

    def change_config(self, new_config):
        global logger

        with open(self.tor_config_path, "w", encoding="utf-8") as config_file:
            config_file.write(new_config.rstrip("\n"))

        logger.info(f"{self.tor_config_path} saved")

    def start(self) -> None:
        global logger

        logger.info("Starting tor thread...")

        self.tor_thread = threading.Thread(target=self.run_tor, daemon=True)
        self.tor_thread.start()

        logger.info("Thread started!")

    def stop(self) -> None:
        global logger

        process = self.tor_process

        if process and process.poll() is None:
            logger.info("Stopping tor...")

            process.terminate()

            logger.info("Tor stopped!")
        else:
            logger.warning("No runned tor process")

    def run_tor(self) -> None:
        global logger

        logger.info("Starting tor process...")

        self.tor_process = subprocess.Popen(
            [self.tor_path, "-f", self.tor_config_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )

        logger.info("Tor started!")

        for line in self.tor_process.stdout:
            # Writes logs to file
            with open(self.tor_logs_file_path, "a", encoding="utf-8") as logs_file:
                # Write line to file
                logs_file.write(line)

            append_logs(line)
