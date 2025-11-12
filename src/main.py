import sys

from ui.pages_controller import PagesController
from ui.main_page import stop_tor


def on_close():
  print("exit")

  stop_tor()

  # Exit from program
  sys.exit(0)


if __name__ == "__main__":
    # Initialize pages controller
    app = PagesController()

    app.protocol("WM_DELETE_WINDOW", on_close)

    # Runs the program
    app.mainloop()
