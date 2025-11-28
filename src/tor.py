import os
import subprocess
import threading

from ui.logs_page import append_logs


class Tor:
    def __init__(self) -> None:
        self.tor_path = "tor\\tor\\tor.exe"
        self.tor_config_path = "tor\\tor\\torrc"

        self.default_config = """
SocksPort localhost:9050
HTTPTunnelPort localhost:8118
"""

        self.tor_thread = None
        self.tor_process = None

    def config_exists(self) -> bool:
        if os.path.exists(self.tor_config_path):
            return True
        else:
            return False

    def create_default_config(self) -> None:
        with open(self.tor_config_path, "w", encoding="utf-8") as config_file:
            config_file.write(self.default_config)

    def get_config(self):
        with open(self.tor_config_path, "r", encoding="utf-8") as config_file:
            config = config_file.read()

        return config

    def change_config(self, new_config):
        with open(self.tor_config_path, "w", encoding="utf-8") as config_file:
            config_file.write(new_config.rstrip("\n"))

    def start(self) -> None:
        self.tor_thread = threading.Thread(target=self.run_tor, daemon=True)
        self.tor_thread.start()

    def stop(self) -> None:
        process = self.tor_process

        if process and process.poll() is None:
            process.terminate()
            print("stopped")

    def run_tor(self) -> None:
        self.tor_process = subprocess.Popen(
            [self.tor_path, "-f", self.tor_config_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )

        print("running")

        for line in self.tor_process.stdout:
            print(line, end="")

            append_logs()

            # Writes logs to file
            with open("logs.txt", "a", encoding="utf-8") as logs_file:
                # Write line to file
                logs_file.write(line)
