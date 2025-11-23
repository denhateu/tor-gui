import tkinter as tk
from tkinter import ttk


class LogsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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

        main_page_button = ttk.Button(
          content_container,
          text="Главная",
          command=lambda: [
            controller.show_main_page()
          ]
        )
        main_page_button.pack()
