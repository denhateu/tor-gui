import tkinter as tk
from tkinter import ttk


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.create_widgets()

    def create_widgets(self):
        # Main container
        main_container = tk.Frame(self)
        main_container.pack(
          anchor="center",
          fill="both",
          expand=True
        )

        # Content container
        content_container = tk.Frame(main_container)
        content_container.pack(
          anchor="center",
          fill="both",
          expand=True
        )

        start_button = ttk.Button(
          content_container,
          text="Запустить"
        )
        start_button.pack()
