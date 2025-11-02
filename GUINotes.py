import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

# window properties
window = tk.Tk()
window.geometry("400x400")
window.maxsize(400, 400)
window.title("Hello World!")
window.config(background="gray")

# icon
icon = tk.PhotoImage(file="DLPGUI/ChudJackSmall.png")
window.iconphoto(True, icon)

# frame padding
frame = ttk.Frame(window, padding=100)
frame.grid()

#image
image = tk.PhotoImage(file="DLPGUI/ChudJackSmall.png")
image_label = tk.Label(frame, image=image).grid(column=1, row=0)

# Label
ttk.Label(frame, text="Billions Must die").grid(column=0, row=0)

# Checkbox
billions_var = tk.BooleanVar()
billions = tk.Checkbutton(frame, text='Billions', variable=billions_var).grid(column=0, row=2)

# OptionMenu
options = ['Millions', 'Billions']
options_var = tk.StringVar(value =options[0])
tk.OptionMenu(frame, options_var, *options).grid(column=0, row=3)

# Define Entry function

input_var = tk.StringVar()

def submit():
    user_input = input_var.get()
    print(user_input)
    #input_var.set("")

# Entry (text field)
tk.Entry(frame, textvariable=input_var).grid(column=0, row=4)

# Normal Button TRUTH NUKE
def truthNuke():
    #print("hello")
    if billions_var.get() and options_var.get() == 'Billions' and input_var.get() == 'Billions':
        window.destroy()
    else:
        tk.messagebox.showinfo("BILLIONS", "BILLIONS")

ttk.Button(frame, text="Truth nuke", command=truthNuke).grid(column=0, row=1)

# Command button
ttk.Button(frame, text='submit', command=submit).grid(column=1, row=4)

# Run window
window.mainloop()
