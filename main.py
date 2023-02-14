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
        self.app.geometry("540x780")

        self.frame = ctk.CTkFrame(master=self.app)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.title = ctk.CTkLabel(master=self.frame, text="YouTube Video Downloder", font=("Elephant", 18), text_color="white")
        self.title.pack(padx=10, pady=10)

        self.title = ctk.CTkLabel(master=self.frame, text="Insert youtube link")
        self.title.pack(padx=10, pady=10)

        
        # Link entry section
        self.frame_1 = ctk.CTkFrame(master=self.frame)
        self.frame_1.columnconfigure(0, weight=1)
        self.frame_1.columnconfigure(1, weight=1)
        
        self.url_var = tk.StringVar()
        self.link = ctk.CTkEntry(master=self.frame_1, width=350, height=40, textvariable=self.url_var, )
        self.link.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.download = ctk.CTkButton(master=self.frame_1, text=u"\u2193",width=10, command=self.downloadQuality)
        self.download.grid(row=0, column=1, sticky=tk.W+tk.E, padx=10)

        self.frame_1.pack(padx=10)

        
        self.finishLabel = ctk.CTkLabel(master=self.frame, text="")
        self.finishLabel.pack()

        # Download percentage
        self.percentage = ctk.CTkLabel(master=self.frame, text="0%")
        self.percentage.pack()

        # Download progress bar
        self.progressBar = ctk.CTkProgressBar(master=self.frame, width=400)
        self.progressBar.set(0)
        self.progressBar.pack()

        # Option Menu
        self.optionMenu = ctk.CTkOptionMenu(self.frame, values=[])
        self.optionMenu.pack(padx=10, pady=10)
        self.optionMenu.set("Download quality")

        # Download button
        self.download = ctk.CTkButton(master=self.frame, text="Download", command=self.startDownload)
        self.download.pack(padx=10, pady=10)

        self.app.mainloop()

    def startDownload(self):
        try:
            self.ytLink = self.link.get()
            ytObject = YouTube(self.ytLink, on_progress_callback=self.onProgress)
            res = self.optionMenu.get()
            video = ytObject.streams.get_by_resolution(res[:4])
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

    def downloadQuality(self):
        getLink = self.link.get()
        ytObject = YouTube(getLink)
        if getLink:
            res = ytObject.streams.filter(file_extension='mp4', progressive=True).order_by('resolution')
            resList = ["144p", "240p", "360p", "720p", "1080p"]
            qualityList = []

            for q in resList:
                if res.get_by_resolution(q):
                    vid = ytObject.streams.get_by_resolution(q)
                    size = round((vid.filesize/(1024**2)),2)
                    qualityList.append(f"{q}   -   {size} MB")
            
            self.optionMenu.configure(values=qualityList)

Downloader()
