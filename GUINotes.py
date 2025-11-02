import tkinter as tk
from tkinter import ttk

# window properties
window = tk.Tk()
window.geometry("700x700")
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

# Normal Button
ttk.Button(frame, text="Truth nuke", command=window.destroy).grid(column=0, row=1)

# Checkbox
tk.Checkbutton(frame, text='Billions').grid(column=0, row=2)

# OptionMenu
options = ['millions', 'billions']
value_inside = tk.StringVar(window)
tk.OptionMenu(frame, value_inside, *options).grid(column=0, row=3)

# Declare variable
input_var = tk.StringVar()

# Define function
def submit():
    user_input = input_var.get()
    print(user_input)
    input_var.set("")

# Entry (text field)
tk.Entry(frame, textvariable=input_var).grid(column=0, row=4)

# Command button
ttk.Button(frame, text='submit', command=submit).grid(column=1, row=4)

# Run window
window.mainloop()
