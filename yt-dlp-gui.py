
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

import os
import subprocess # used for cmd commands in py
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

def submit_url():
    command = create_command()
    url = wv_input_var.get()
    if not url:
        wv_message.set("No URL Entered")
        return

    # calls and sets the msg 
    result = subprocess.getoutput(command +" "+ url)
    wv_message.set(result)


# submit url helper
def create_command():
    command = "yt-dlp.exe"

    # file type
    if wv_ftOption.get() != "Select a file type":
        command += " -t " + wv_ftOption.get().lower()

    # quality
    if wv_qualOption.get() != "Select video quality":
        command += f' -S "res:{wv_qualOption.get()}"'

    # Subtitles
    if wv_subtitles.get():
        command += " --write-subs --sub-lang en"


    print(command)
    return command


def create_widgets(window):
    global wv_message, wv_input_var, wv_ftOption, wv_qualOption, wv_subtitles

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
    wv_ftOption = tk.StringVar(value="Select a file type")
    btn_fileType = tk.OptionMenu(window, wv_ftOption, *fileTypes)
    btn_fileType.pack(pady=5)

    # Dropdown for video quality
    quality = ["Select video quality","2160","1440","1920", "720", "480"]
    wv_qualOption = tk.StringVar(value="Select video quality")
    btn_fileType = tk.OptionMenu(window, wv_qualOption, *quality)
    btn_fileType.pack(pady=5)

    # checkbox for subtitles
    wv_subtitles = tk.BooleanVar(value=0)
    btn_subtitles = tk.Checkbutton(window, variable=wv_subtitles, text="subtitles")
    btn_subtitles.pack(pady=5)



def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("WORKING DIR:", os.getcwd())


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
