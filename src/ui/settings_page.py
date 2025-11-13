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

        self.config_textarea = tk.Text(content_container)
        self.config_textarea.pack()

        self.config_textarea.insert(tk.END, self.get_config())

        save_button = ttk.Button(
          content_container,
          text="Сохранить",
          command=lambda: [
            self.save_config()
          ]
        )
        save_button.pack()

    def get_config(self):
      with open("tor\\tor\\torrc", 'r', encoding="utf-8") as config_file:
        config = config_file.read()

      return config

    def save_config(self):
      # Gets config from textarea
      textarea_config = self.config_textarea.get("1.0", tk.END)
      print(textarea_config)

      # Saves config to file
      with open("tor\\tor\\torrc", 'w', encoding="utf-8") as config_file:
        config_file.write(textarea_config)
