import tkinter as tk
from tkinter import ttk


logs_textarea = None


def append_logs():
    with open("logs.txt", "r", encoding="utf-8") as logs_file:
        all_logs = logs_file.read()

    global logs_textarea

    # Clear Text widged
    logs_textarea.delete("1.0", tk.END)

    # Append logs to clear Text widged
    logs_textarea.insert("end", all_logs)


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
