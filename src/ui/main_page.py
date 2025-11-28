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

        global tor

        self.control_button = ttk.Button(
          content_container,
          text="Запустить",
          command=lambda: [
            self.toggle_buttons(mode="stop"),
            tor.start()
          ]
        )
        self.control_button.pack()

        settings_button = ttk.Button(
          content_container,
          text="Настройки",
          command=lambda: [
            controller.show_frame(SettingsPage)
          ]
        )
        settings_button.pack()

        logs_button = ttk.Button(
          content_container,
          text="Логи",
          command=lambda: [
            controller.show_frame(LogsPage)
          ]
        )
        logs_button.pack()

    def toggle_buttons(self, mode="stop"):
      global tor

      if mode == "start":
        self.control_button.config(
            text="Запустить",
            command=lambda: [
              self.toggle_buttons(mode="stop"),
              tor.start()
            ]
        )
      elif mode == "stop":
        self.control_button.config(
            text="Стоп",
            command=lambda: [
              self.toggle_buttons(mode="start"),
              tor.stop()
            ]
        )
