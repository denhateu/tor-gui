import tkinter as tk
from tkinter import ttk
import threading
import subprocess

from .settings_page import SettingsPage
from .logs_page import LogsPage, append_logs


# Global variable for process
process = None


def run_tor():
    global process
    process = subprocess.Popen(
      ["tor\\tor\\tor.exe", "-f", "tor\\tor\\torrc"],
      stdout=subprocess.PIPE,
      stderr=subprocess.STDOUT,
      text=True
    )

    print("running")

    for line in process.stdout:
      print(line, end="")

      # Writes logs to file
      with open("logs.txt", 'a', encoding="utf-8") as logs_file:
        # Write line to file
        logs_file.write(line)

      append_logs()

def stop_tor():
    global process
    if process and process.poll() is None:
      process.terminate()
      print("stopped")


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

        self.control_button = ttk.Button(
          content_container,
          text="Запустить",
          command=lambda: [
            self.toggle_buttons(mode="stop"),
            self.start_thread()
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
      if mode == "start":
        self.control_button.config(
            text="Запустить",
            command=lambda: [
              self.toggle_buttons(mode="stop"),
              self.start_thread()
            ]
        )
      elif mode == "stop":
        self.control_button.config(
            text="Стоп",
            command=lambda: [
              self.toggle_buttons(mode="start"),
              stop_tor()
            ]
        )

    def start_thread(self):
      thread = threading.Thread(target=run_tor, daemon=True)
      thread.start()
