import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os
import subprocess # used for cmd commands in py

# FOR INSTALLING FFMPEG
# winget install "FFmpeg (Essentials Build)"

# window properties
window = tk.Tk()
window.geometry("400x350")
window.resizable(width=False, height=False)
window.title("ChudJack.exe")
window.config(background="gray")

# frame padding
frame = ttk.Frame(window, padding=100)
frame.grid()

###################### WIDGETS #######################

#icon

image_path = "DLPGUI\ChudJackSmall.png"
image_path2 = "ChudJackSmall.png"

if os.path.exists(image_path):
    icon = tk.PhotoImage(file=image_path)
    window.iconphoto(True, icon)
elif os.path.exists(image_path2):
    icon = tk.PhotoImage(file=image_path2)
    window.iconphoto(True, icon)
else:
    pass



# Normal Button TRUTH NUKE
def truthNuke():
    #print("hello")
    if billions_var.get() and options_var.get() == 'Billions' and input_var.get() == 'Billions':
        window.destroy()
    else:
        tk.messagebox.showinfo("Try Again", "Billions, chuddy. Better believe it.\nInitiate the Billions")

#Entry
def submit():
    user_input = input_var.get()
    print(user_input)
    #input_var.set("")

#image
if os.path.exists(image_path):
    image = tk.PhotoImage(file=image_path)
    image_label = tk.Label(frame, image=image).grid(column=1, row=0)
elif os.path.exists(image_path2):
    image = tk.PhotoImage(file=image_path2)
    image_label = tk.Label(frame, image=image).grid(column=1, row=0)
else:
    print("Image failed to load:")

# Label
ttk.Label(frame, text="Billions Must die").grid(column=0, row=0)

# Checkbox
billions_var = tk.BooleanVar()
billions = tk.Checkbutton(frame, text='Billions', variable=billions_var).grid(column=0, row=2)

# OptionMenu
options = ['Millions', 'Billions']
options_var = tk.StringVar(value =options[0])
tk.OptionMenu(frame, options_var, *options).grid(column=0, row=3)

# Entry (text field)
# Define Entry function
input_var = tk.StringVar()
tk.Entry(frame, textvariable=input_var).grid(column=0, row=4)

# Normal Button TRUTH NUKE
ttk.Button(frame, text="Truth nuke", command=truthNuke).grid(column=0, row=1)

# Command button
ttk.Button(frame, text='submit', command=submit).grid(column=1, row=4)

# Run window
window.mainloop()
