
####################################################
# TODO: # Add dropdown for subtitles
#       # Add dropdown for vid quality
#       # Add dropdown for MP4 / MP3 / other
#       # wf_submitURL functionality
#       # Download bar
#       # if no FFMPEG downloaded, prompt user if they want to download
#       # Multi download?
#       # Multi threaded?
#       # Learn more about yt-dlp downloader for more funcitonality
####################################################

import os
import subprocess # used for cmd commands in py
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

def submit_url():
    url = wv_input_var.get()
    if not url:
        tkinter.messagebox.showerror("Error", "Enter a valid URL!")
        return
    wv_message.set(f"Submitted: {url}")

    # Call yt-dlp.exe with a URL
    subprocess.run(["DLPGUI\yt-dlp.exe", url])

def create_widgets(window):
    global wv_input_var, wv_message

    # top message
    wv_message = tk.StringVar(value="Welcome")
    message = tk.Label(window, textvariable=wv_message, bg="lightblue", height=3, width=50)
    message.pack(pady=20)

    # url + submit widget
    wv_input_var = tk.StringVar()
    w_urlEnter = tk.Entry(window, textvariable=wv_input_var, borderwidth=2, width = 60)
    w_urlSubmit = ttk.Button(window, text="Submit", command=submit_url)

    w_urlEnter.pack()
    w_urlSubmit.pack()

def main():
    #create window
    window = tk.Tk()
    window.geometry("400x400")
    window.resizable(width=False, height=False)
    window.title("YT-dlp-gui")
    window.config(background="gray")

    create_widgets(window)

    window.mainloop()

if __name__ == "__main__":
    main()
