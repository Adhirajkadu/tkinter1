from tkinter import *

root = Tk()
root.title('main')
root.geometry('400x300')

def topwin():
    top = Toplevel()
    top.title('Login App')
    top.geometry('100x100')

    l2 = Label(top, text="This is top level window")
    l2.pack()

    top.mainloop()

l = Label(root, text="This is root window")
btn = Button(root, text="click here to open another window", command=topwin)

l.pack()
btn.pack()

root.mainloop()