from tkinter import *

def calculate_product():
    num1=int(entry1.get())
    num2=int(entry2.get())
    product=num1*num2
    result_label.configure(text="Product"+ str(product))

root=Tk()
root.title("Product Calculator")
root.geometry("300x200")

Label(root, text="Enter Length :").pack(pady=5)
entry1=Entry(root)
entry1.pack()

Label(root, text="Enter Second Length: ").pack(pady=5)
entry2=Entry(root)
entry2.pack()

Button(root, text="Calculate Product", command=calculate_product).pack(pady=10)

result_label=Label(root, text="Product = ")
result_label.pack()

root.mainloop()