
####################################################
# TODO: # Add functionality for subtitles
#       # Add functionality for vid quality
#       # Add functionality for MP4 / MP3 / other
#       # Download bar but actually working, i think the gui and backend have to be seperate threads
#       # Custom file path download with a browse
#
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

    # calls and sets the msg in one line
    wv_message.set(subprocess.getoutput(["DLPGUI\yt-dlp.exe", url]))

def create_widgets(window):
    global wv_input_var, wv_message

    # top message
    wv_message = tk.StringVar(value="Welcome")
    message = tk.Label(window, textvariable=wv_message, bg="lightblue", height=3, width=50)
    message.pack(pady=20)

    # url + submit widget
    wv_input_var = tk.StringVar()
    btn_urlEnter = tk.Entry(window, textvariable=wv_input_var, borderwidth=2, width = 60)
    btn_urlSubmit = ttk.Button(window, text="Submit", command=submit_url)
    btn_urlEnter.pack()
    btn_urlSubmit.pack(pady=5)

    # Dropdown for file Type
    fileTypes = ["Select a file type","MP4", "MP3"]
    wv_ftoption = tk.StringVar(value="Select a file type")
    btn_fileType = tk.OptionMenu(window, wv_ftoption, *fileTypes)
    btn_fileType.pack(pady=5)

    # Dropdown for video quality
    quality = ["Select video quality","Best", "Worst"]
    wv_option = tk.StringVar(value="Select video quality")
    btn_fileType = tk.OptionMenu(window, wv_option, *quality)
    btn_fileType.pack(pady=5)

    # checkbox for subtitles
    wv_subtitles = tk.BooleanVar(value=0)
    btn_subtitles = tk.Checkbutton(window, variable=wv_subtitles, text="subtitles")
    btn_subtitles.pack(pady=5)



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
