import sys

from tor import Tor
from ui.pages_controller import PagesController


tor = Tor()


def on_close() -> None:
  print("exit")

  global tor
  tor.stop()

  # Exit from program
  sys.exit(0)


if __name__ == "__main__":
    # Checks if config not found then create new config
    if not tor.config_exists():
      tor.create_default_config()

    # Initialize pages controller
    app = PagesController()

    app.protocol("WM_DELETE_WINDOW", on_close)

    # Runs the program
    app.mainloop()
