import tkinter as tk
from tkinter import ttk


class SettingsPage(tk.Frame):
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

        settings_button = ttk.Button(
          content_container,
          text="Главная",
          command=lambda: [
            controller.show_main_page()
          ]
        )
        settings_button.pack()

        config_textarea = tk.Text(content_container)
        config_textarea.pack()

        config_textarea.insert(tk.END, self.get_config())

    def get_config(self):
      with open("tor\\tor\\torrc", 'r', encoding="utf-8") as config_file:
        config = config_file.read()

      return config
