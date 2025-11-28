import tkinter as tk
from tkinter import ttk

from tor import Tor


tor = Tor()


class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Main container
        main_container = tk.Frame(self)
        main_container.pack(anchor="center", fill="both", expand=True)

        # Content container
        content_container = tk.Frame(main_container)
        content_container.pack(anchor="center", fill="both", expand=True)

        main_page_button = ttk.Button(
            content_container,
            text="Главная",
            command=lambda: [controller.show_main_page()],
        )
        main_page_button.pack()

        self.config_textarea = tk.Text(content_container)
        self.config_textarea.pack()

        global tor
        self.config_textarea.insert(tk.END, tor.get_config())

        save_button = ttk.Button(
            content_container, text="Сохранить", command=lambda: [self.save_config()]
        )
        save_button.pack()

    def save_config(self):
        # Gets config from textarea
        textarea_config = self.config_textarea.get("1.0", tk.END)

        # Saves new config
        global tor
        tor.change_config(textarea_config)
