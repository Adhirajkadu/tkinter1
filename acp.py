from tkinter import *
from datetime import date

def calculate_age():
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    today = date.today()

    age = today.year - year

    if(today.month, today.day) < (month, day):
        age -= 1

        result_label.config(text="Presrnt Age = " + "years")

root = Tk()
root.title("Age Calculate")
root.geometry("350x250")

Label(root, text="Enter Birth Date: ").pack(pady=5)
day_entry = Entry(root)
day_entry.pack()

Label(root, text="Enter Birth Month: ").pack(pady=5)
month_entry = Entry(root)
month_entry.pack()

Label(root, text="Enter Birth Year: ").pack(pady=5)
year_entry = Entry(root)
year_entry.pack()

Button(root, text="Calculate Age", command=calculate_age).pack(pady=15)

result_label = Label(root, text="Present Age = ")
result_label.pack()

root.mainloop()