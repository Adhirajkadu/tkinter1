from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Virus")
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found")

button = Button(root, text="Searching for Virus", command=msg)
button.place(x=40, y=80)

root.mainloop()