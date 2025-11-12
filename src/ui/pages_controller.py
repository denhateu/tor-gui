import tkinter as tk

from .main_page import MainPage
from .empty_page import EmptyPage
from .settings_page import SettingsPage


class PagesController(tk.Tk):
    """This simple class is used to switch between windows
    in the program, this class needs no modification
    """

    def show_frame(self, frame_container):
        """This function opens the received frame in full screen mode

        Args:
            frame_container:
                Name of the frame class to open
        """

        frame = self.frames[frame_container]
        frame.tkraise()

    def show_main_page(self):
        frame = self.frames[MainPage]
        frame.tkraise()

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Create main full screen frame
        container = tk.Frame(self)
        container.pack(
            side = "top",
            fill = "both",
            expand = True
        )

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        # Initializing frames to an empty array
        self.frames = {}

        # Write all frame class names to frames variable for switching
        for frame in (MainPage, EmptyPage, SettingsPage):
            current_frame = frame(container, self)

            self.frames[frame] = current_frame

            current_frame.grid(
                column = 0,
                row = 0,
                sticky = "nsew"
            )

        # Open default frame
        self.show_frame(MainPage)
