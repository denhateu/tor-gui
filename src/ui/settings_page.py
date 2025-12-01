import tkinter as tk
from tkinter import ttk

from tor import Tor


tor = Tor()


class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Main container
        main_container = tk.Frame(self)
        main_container.pack(
            padx=15,
            pady=15,
            fill="both",
            expand=True
        )

        # Header container
        header_container = tk.Frame(
            main_container
        )
        header_container.pack(
            pady = (0, 15),
            side="top",
            anchor="n",
            fill="x",
        )

        header_inner_container = tk.Frame(
            header_container,
        )
        header_inner_container.pack(
            fill="x",
            expand=True
        )

        header_inner_container.columnconfigure(index=0, weight=1)
        header_inner_container.rowconfigure(index=0, weight=1)

        main_page_button = ttk.Button(
            header_inner_container,
            text="Главная",
            command=lambda: [controller.show_main_page()],
        )
        main_page_button.grid(
            sticky="nw",
            column=0,
            row=0
        )

        # Content container
        content_container = tk.Frame(main_container)
        content_container.pack(anchor="center", fill="both", expand=True)

        tk.Label(
            content_container,
            text="Настройки",
            font=("Consolas", 22, "bold")
        ).pack(
            pady=(0, 5),
            anchor="w"
        )

        self.config_textarea = tk.Text(content_container)
        self.config_textarea.pack(
            pady=(0, 5),
            fill="both",
            expand=True
        )

        global tor
        self.config_textarea.insert(tk.END, tor.get_config())

        save_button = ttk.Button(
            content_container,
            text="Сохранить",
            command=lambda: [self.save_config()]
        )
        save_button.pack(
            ipadx=5,
            ipady=5,
            fill="x"
        )

    def save_config(self):
        # Gets config from textarea
        textarea_config = self.config_textarea.get("1.0", tk.END)

        # Saves new config
        global tor
        tor.change_config(textarea_config)
