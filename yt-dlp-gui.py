
####################################################
# TODO: # add different languages for subtitles
#       # Custom file path download with a browse
#
#       # Multi download?
#       # Learn more about yt-dlp downloader for more funcitonality
####################################################

#Commands for later
# --console-title  Display progress in console titlebar
# # winget install "FFmpeg (Essentials Build)"

import os
import subprocess # used for cmd commands in py
from threading import *
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def submit_url():
    global submit_running, result
    submit_running = True
    result = "Starting..."

    command = create_command()
    if not command:
        submit_running = False
        return

    # Start the process
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        shell=True
    )

    # Stream output
    for line in process.stdout:
        result = line.strip()

    process.wait()
    submit_running = False

# gives user a update on the download
def update_submit_msg():
    if submit_running:
        wv_message.set(result)
        window.after(500, update_submit_msg)
    else:
        wv_message.set("Download Complete.")
        


# submit url helper 1
def submit_url_threading():
    t1 = Thread(target = submit_url)
    t1.start()
    update_submit_msg()



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


def create_widgets():
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


def verify_dependencies():
    #FFMPEG
    try:
        result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True, check=True)
        print("FFmpeg is installed and accessible.")
    except FileNotFoundError | subprocess.CalledProcessError:
        print("ERROR: FFmpeg is not installed or not in the PATH.")
        messagebox.showerror("FFmpeg is not installed, not in the PATH or corrupt.",
        "\nPlease run \" winget install \"FFmpeg (Essentials Build)\" \" in cmd " \
        " this program will not act properly without it")
        window.destroy()
    
    #yt-dlp.exe
    ytdlp = os.path.exists(os.getcwd() + "\yt-dlp.exe")
  
    if ytdlp:
        print("yt-dlp.exe found")
    else:
        print("ERROR: yt-dlp.exe not found")
        messagebox.showerror("yt-dlp.exe is not found in the main file", 
                             "yt-dlp.exe is not found in the main file\n please reinstall from github")
        window.destroy()
       

def main():
    global window

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("WORKING DIR:", os.getcwd())

    #create window
    window = tk.Tk()
    window.geometry("640x320")
    window.resizable(width=False, height=False)
    window.title("YT-dlp-gui")
    window.config(background="gray")

    verify_dependencies()

    create_widgets()

    window.mainloop()

if __name__ == "__main__":
    main()
