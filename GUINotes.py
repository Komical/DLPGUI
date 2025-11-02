import tkinter
from tkinter import *
from tkinter import ttk

# widgets = GUI elements : buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

#window properties
window = Tk() # instantiate an instance of a window
window.geometry("500x500") # Change size
window.title("Hello World!")
window.config(background="gray")

#icon
icon = PhotoImage(file="ChudJack.png")
window.iconphoto(True, icon)

#frame padding
frame = ttk.Frame(padding=100)
frame.grid()

#how to do text
ttk.Label(frame, text="Hello World!").grid(column=0,row=0)

#Normal Button
ttk.Button(frame, text="Quit", command=window.destroy).grid(column=0, row=1)

#Checkbox
Checkbutton(frame, text ='Hello?').grid(column=0, row=2)

#OptionMenu
options = ['option1', 'option2']
value_inside = tkinter.StringVar(window)
OptionMenu(frame, value_inside, *options).grid(column=0, row=3)

#EnterText

#declare variable
input_var = tkinter.StringVar()

#define function that will be a command later
def submit():
    user_input = input_var.get()

    print(user_input)
    input_var.set("")

#enter text here
user_entry = Entry(frame, textvariable= input_var).grid(column=0, row=4)

#command setter button
submit_btn = ttk.Button(frame,text = 'submit ^', command = submit).grid(column=2,row=4)


#how to look at all the commands for something, make sure to put .configure()
#print(ttk.Button().configure())
window.mainloop() # place window on screen, listen for events

