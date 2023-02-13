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

        self.finishLabel = ctk.CTkLabel(self.app, text="")
        self.finishLabel.pack()

        # Download percentage
        self.percentage = ctk.CTkLabel(self.app, text="0%")
        self.percentage.pack()

        # Download progress bar
        self.progressBar = ctk.CTkProgressBar(self.app, width=400)
        self.progressBar.set(0)
        self.progressBar.pack()

        self.download = ctk.CTkButton(self.app, text="Download", command=self.startDownload)
        self.download.pack(padx=10, pady=10)

        self.app.mainloop()

    def startDownload(self):
        try:
            ytLink = self.link.get()
            ytObject = YouTube(ytLink, on_progress_callback=self.onProgress)
            video = ytObject.streams.get_lowest_resolution()
            self.title.configure(text=ytObject.title, text_color="white")
            self.finishLabel.configure(text="")
            video.download()
            self.finishLabel.configure(text=" Downloded!")
        except:
            self.finishLabel.configure(text="Download Error", text_color="red")

    def onProgress(self, stream, chunk, bytes_remaining):
        totalSize = stream.filesize
        bytes_downloded = totalSize - bytes_remaining
        percentageOfCompletion = bytes_downloded/totalSize * 100
        per = str(int(percentageOfCompletion))
        self.percentage.configure(text = per + "%")
        self.percentage.update()

        self.progressBar.set(float(percentageOfCompletion)/100)

Downloader()
