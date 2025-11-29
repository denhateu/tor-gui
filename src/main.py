import sys

from logging_setup import setup_logging
from tor import Tor
from ui.pages_controller import PagesController


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

    app.protocol("WM_DELETE_WINDOW", on_close)

    # Runs the program
    app.mainloop()
