from tkinter import *
from tkinter import messagebox
import random

def play(user):
    choices=["Rock", "Paper", "Scissors"]
    computer=random.choice(choices)

    if user==computer:
        result="It's a Tie!"
    elif(user=="Rock" and computer=="Scissors") or (user=="Paper" and computer=="Rock") or (user=="Scissors" and computer=="Paper"):
        result="You Wins!"
    else:
        result="Computer Wins!"

    messagebox.showinfo("Result", f"Your Choice: {computer}\n\n{result}")

root=Tk()
root.title("Rock Paper Scissors")
root.geometry("300x250")

label=Label(root, text="Rock Paper Scissors", font=("Arial", 16))
label.pack(pady=20)

btn1=Button(root, text="Rock", width=15, command=lambda:play("Rock"))
btn1.pack(pady=5)

btn2=Button(root, text="Paper", width=15, command=lambda:play("Paper"))
btn2.pack(pady=5)

btn3=Button(root, text="Scissors", width=15, command=lambda:play("Scissors"))
btn3.pack(pady=5)

root.mainloop()