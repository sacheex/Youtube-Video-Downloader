import tkinter as tk
import customtkinter as ctk
from pytube import YouTube

class Downloader:
    def __init__(self):

        # System settings
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Framework
        self.app = ctk.CTk()

        self.app.title("Youtube Video Downloader")
        self.app.geometry("720x480")

        self.title = ctk.CTkLabel(self.app, text="Insert youtube link")
        self.title.pack(padx=10, pady=10)

        self.url_var = tk.StringVar()
        self.link = ctk.CTkEntry(self.app, width=350, height=40, textvariable=self.url_var)
        self.link.pack()

        self.download = ctk.CTkButton







        self.app.mainloop()

Downloader()