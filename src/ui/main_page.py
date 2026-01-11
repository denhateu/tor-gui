import tkinter as tk
from tkinter import ttk

from tor import Tor
from .settings_page import SettingsPage
from .logs_page import LogsPage


tor = Tor()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global tor

        tor.set_status_callback(self.on_update_status)
        tor.set_status_percentage_callback(self.on_update_status_percentage)

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
            fg="#f0e035"
        )
        self.progress_label.grid(
            sticky="w",
            column=1,
            row=0
        )

    def toggle_buttons(self, mode="stop"):
        global tor

        if mode == "start" or mode == "stopped":
            self.control_button.config(
                text="Запустить",
                command=lambda: [
                    self.toggle_buttons(mode="stop"),
                    tor.start()
                ],
            )
        elif mode == "stop":
            self.control_button.config(
                text="Стоп",
                command=lambda: [self.toggle_buttons(mode="start"), tor.stop()],
            )

    def on_update_status(self, status):
        self.after(0, self.update_status, status)
        self.after(0, self.toggle_buttons, status)

    def on_update_status_percentage(self, percentage):
        self.after(0, self.update_progress_label, percentage)

    def update_status(self, status):
        if status == "connecting":
            self.status_label.config(text="Подключение", fg="#f0e035")
            self.progress_label.config(text="0%")
        elif status == "running":
            self.status_label.config(text="Запущен", fg="#29e314")
            self.progress_label.config(text="")
        elif status == "stopped":
            self.status_label.config(text="Выключен", fg="red")
            self.progress_label.config(text="")

    def update_progress_label(self, percentage):
        self.progress_label.config(text=percentage)
