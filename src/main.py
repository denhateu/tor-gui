import sys
import os

from ui.pages_controller import PagesController
from ui.main_page import stop_tor


def on_close():
  print("exit")

  stop_tor()

  # Exit from program
  sys.exit(0)


if __name__ == "__main__":
    # Checks if config not found then create new config
    if not os.path.exists("tor\\tor\\torrc"):
      print("Config not found, creates new config")

      default_config = """
SocksPort localhost:9050
HTTPTunnelPort localhost:8118
"""
      with open("tor\\tor\\torrc", 'w', encoding="utf-8") as config_file:
        config_file.write(default_config)

    # Initialize pages controller
    app = PagesController()

    app.protocol("WM_DELETE_WINDOW", on_close)

    # Runs the program
    app.mainloop()
