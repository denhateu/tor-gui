import tkinter as tk
from tkinter import ttk

from tor import Tor
from .settings_page import SettingsPage
from .logs_page import LogsPage


tor = Tor()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Main container
        main_container = tk.Frame(self)
        main_container.pack(
            padx=15,
            pady=15,
            anchor="center",
            fill="both",
            expand=True
        )

        # Header container
        header_container = tk.Frame(
            main_container
        )
        header_container.pack(
            side="top",
            anchor="n",
            fill="x",
        )

        header_inner_container = tk.Frame(
            header_container
        )
        header_inner_container.pack(
            fill="x",
            expand=True
        )

        header_inner_container.columnconfigure(index=(0, 1), weight=1)
        header_inner_container.rowconfigure(index=0, weight=1)

        settings_button = ttk.Button(
            header_inner_container,
            text="Настройки",
            command=lambda: [controller.show_frame(SettingsPage)],
        )
        settings_button.grid(
            sticky="nw",
            column=0,
            row=0
        )

        logs_button = ttk.Button(
            header_inner_container,
            text="Логи",
            command=lambda: [controller.show_frame(LogsPage)],
        )
        logs_button.grid(
            sticky="ne",
            column=1,
            row=0
        )

        # Content container
        content_container = tk.Frame(
            main_container,
        )
        content_container.pack(anchor="center", fill="both", expand=True)

        global tor

        self.control_button = ttk.Button(
            content_container,
            text="Запустить",
            command=lambda: [self.toggle_buttons(mode="stop"), tor.start()],
        )
        self.control_button.pack(
            ipadx=30,
            ipady=30,
            anchor="center",
            expand=True
        )

        """
        status_container = tk.Frame(
            content_container
        )
        status_container.pack(
            side="bottom",
            anchor="s"
        )

        status_container.columnconfigure(index=(0, 1), weight=1)
        status_container.rowconfigure(index=0, weight=1)

        self.status_label = tk.Label(
            status_container,
            text="Выключен",
            font=("", 14),
            fg="red"
        )
        self.status_label.grid(
            sticky="e",
            column=0,
            row=0
        )

        self.progress_label = tk.Label(
            status_container,
            font=("", 14),
            fg="yellow"
        )
        self.progress_label.grid(
            sticky="w",
            column=1,
            row=0
        )
        """

    def toggle_buttons(self, mode="stop"):
        global tor

        if mode == "start":
            self.control_button.config(
                text="Запустить",
                command=lambda: [
                    self.toggle_buttons(mode="stop"),
                    tor.start()
                ],
            )

            """
            self.status_label.config(
                text="Выключен",
                fg="red"
            )
            """
        elif mode == "stop":
            self.control_button.config(
                text="Стоп",
                command=lambda: [self.toggle_buttons(mode="start"), tor.stop()],
            )

            """
            self.status_label.config(
                text="Подключение",
                fg="yellow"
            )
            """
