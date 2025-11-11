import tkinter as tk
from tkinter import ttk
import threading
import subprocess


# Global variable for process
process = None


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

        self.control_button = ttk.Button(
          content_container,
          text="Запустить",
          command=lambda: [
            self.toggle_buttons(mode="stop"),
            self.start_thread()
          ]
        )
        self.control_button.pack()

    def toggle_buttons(self, mode="stop"):
      print(mode)

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
              self.stop_tor()
            ]
        )

    def run_tor(self):
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

    def stop_tor(self):
      global process
      if process and process.poll() is None:
        process.terminate()
        print("stopped")

    def start_thread(self):
      thread = threading.Thread(target=self.run_tor, daemon=True)
      thread.start()
