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
        main_container = tk.Frame(
            self,
        )
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
        content_container = tk.Frame(
            main_container
        )
        content_container.pack(anchor="center", fill="both", expand=True)

        tk.Label(
            content_container,
            text="Логи",
            font=("Consolas", 22, "bold")
        ).pack(
            pady=(0, 5),
            anchor="w"
        )

        global logs_textarea
        logs_textarea = tk.Text(content_container)
        logs_textarea.pack(
            fill="both",
            expand=True
        )
