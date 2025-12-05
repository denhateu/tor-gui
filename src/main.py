import sys

from config import WINDOW_TITLE
from logging_setup import setup_logging
from tor import Tor
from ui.pages_controller import PagesController
from screen_size import get_screen_size


# Setup logging
logger = setup_logging()

tor = Tor()


def on_close() -> None:
    global tor
    tor.stop()

    global logger
    logger.info("Exit...")

    # Exit from program
    sys.exit(0)


if __name__ == "__main__":
    # Checks if config not found then create new config
    if tor.config_exists():
        logger.info("Tor config file found")
    else:
        logger.warning("Tor config file not found, create new config")

        tor.create_default_config()

        logger.info("New Tor config created!")

    # Initialize pages controller
    app = PagesController()

    # Configure window
    app.title(WINDOW_TITLE)

    # Gets screen sizes (width, height) in pixels
    screen_size = get_screen_size()

    # Gets 1/2 of screen sizes
    window_width = screen_size[0] // 2
    window_height = screen_size[1] // 2

    # Center of screen points
    position_x = (screen_size[0] - window_width) // 2
    position_y = (screen_size[1] - window_height) // 2

    app.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    app.protocol("WM_DELETE_WINDOW", on_close)

    # Runs the program
    app.mainloop()
