import tkinter as tk
from tkinter import ttk


logs_textarea = None


def append_logs(log_string):
    global logs_textarea

    # Append logs to textarea
    logs_textarea.insert(tk.END, log_string)

    # Automatically scroll to the bottom to show the newest logs
    logs_textarea.see(tk.END)


class LogsPage(tk.Frame):
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

        global logs_textarea
        logs_textarea = tk.Text(content_container)
        logs_textarea.pack()
