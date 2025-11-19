
####################################################
# TODO: # add different languages for subtitles
#       # Download bar but actually working, i think the gui and backend have to be seperate threads
#       # Custom file path download with a browse
#
#       # if no FFMPEG downloaded, prompt user if they want to download
#       # Multi download?
#       # Multi threaded?
#       # Learn more about yt-dlp downloader for more funcitonality
####################################################

#Commands for later
# --console-title  Display progress in console titlebar
# # winget install "FFmpeg (Essentials Build)"

import os
import subprocess # used for cmd commands in py
from threading import *
import tkinter as tk
from tkinter import ttk


def submit_url():
    command = create_command()

    if command:
        # calls and sets the msg 
        wv_message.set("Downloading . . .")
        result = subprocess.getoutput(command)
        wv_message.set(result)
        print(result)

    wv_input_var.set("")

# submit url helper 1
def submit_url_threading():
    t1 = Thread(target = submit_url)
    t1.start()

# submit url helper 2
def create_command():
    command = "yt-dlp.exe"
    
    #URL
    url = wv_input_var.get()
    if not url:
        wv_message.set("No URL Entered")
        return
    
    # file type
    if wv_ftOption.get() != "Select a file type":
        command += " -t " + wv_ftOption.get().lower()
    else:
        wv_message.set("No file type selected")
        return

    # quality
    if wv_qualOption.get() != "Select video quality":
        command += f' -S "res:{wv_qualOption.get()}"'
    else:
        wv_message.set("No Quality selected")
        return

    # Subtitles
    if wv_subtitles.get():
        command += " --write-subs --sub-lang en "

    command += " " + url
    print(command)
    return command


def create_widgets(window):
    global wv_message, wv_input_var, wv_ftOption, wv_qualOption, wv_subtitles

    # top message
    wv_message = tk.StringVar(value="Welcome")
    message = tk.Label(window, textvariable=wv_message, bg="lightblue", height=8, width=70)
    message.pack(pady=20)

    # url + submit widget
    label_URL = tk.Label(window, text="URL:")
    wv_input_var = tk.StringVar()
    btn_urlEnter = tk.Entry(window, textvariable=wv_input_var, borderwidth=2, width= 85)
    btn_urlSubmit = ttk.Button(window, text="Submit", command=submit_url_threading)
    
    # Dropdown for file Type
    fileTypes = ["Select a file type","MP4", "MP3"]
    wv_ftOption = tk.StringVar(value="Select a file type")
    btn_fileType = tk.OptionMenu(window, wv_ftOption, *fileTypes)
    

    # Dropdown for video quality
    quality = ["Select video quality","2160","1440","1920", "720", "480", "240", "144"]
    wv_qualOption = tk.StringVar(value="Select video quality")
    btn_quality = tk.OptionMenu(window, wv_qualOption, *quality)

    # checkbox for subtitles
    wv_subtitles = tk.BooleanVar(value=0)
    btn_subtitles = tk.Checkbutton(window, variable=wv_subtitles, text="subtitles")
    
    # Packing
    btn_fileType.pack(pady=5)
    btn_quality.pack(pady=5)
    btn_subtitles.pack(pady=5)
    label_URL.pack(anchor="sw", side="left", padx=5, pady=5)
    btn_urlEnter.pack(anchor="sw", side="left", padx=5, pady=5)
    btn_urlSubmit.pack(anchor = "sw", side = "right", padx=5, pady=5, fill="x")


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("WORKING DIR:", os.getcwd())


    #create window
    window = tk.Tk()
    window.geometry("640x320")
    window.resizable(width=False, height=False)
    window.title("YT-dlp-gui")
    window.config(background="gray")

    create_widgets(window)

    window.mainloop()

if __name__ == "__main__":
    main()
