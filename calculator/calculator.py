from tkinter import *
from math import sqrt
root = Tk()
root.title("Simple Calculator")

large_font = ('Verdana', 30)
e = Entry(root, borderwidth=5, width=10, font=large_font)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def calc_back():
    current= e.get()
    current = current[:-1]
    e.delete(0, END)
    e.insert(0, current)

def calc_clear():
    e.delete(0, END)

def calc_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def calc_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def calc_multiply():
    first_number =e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def calc_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def calc_percent():
    first_number = e.get()
    global f_num
    global math
    math = "percentage"
    f_num = int(first_number)
    e.delete(0, END)

def calc_ofx():
    first_number = e.get()
    e.delete(0, END)
    e.insert(0, 1/int(first_number))

def calc_square():
    first_number = int(e.get())
    e.delete(0, END)
    e.insert(0, first_number * first_number)

def calc_square_root():
    first_number = int(e.get())
    e.delete(0, END)
    e.insert(0, sqrt(first_number))


def calc_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))

    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))

    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))

    elif math == "division":
        e.insert(0, f_num / int(second_number))
    elif math == "percentage":
        e.insert(0, f_num * (int(second_number)/100))


# DEFINE BUTTONS
button_percent = Button(root, text="%", padx=43, pady=20, command=calc_percent)
button_back = Button(root, text="B", padx=40, pady=20, command=calc_back)
button_clear = Button(root, text="C", padx=93, pady=20, command=calc_clear)

button_ofx = Button(root, text="1/x", padx=40, pady=20, command=calc_ofx)
button_square = Button(root, text="x^2", padx=40, pady=20, command=calc_square)
button_square_root = Button(root, text="√", padx=40, pady=20, command=calc_square_root)
button_divide = Button(root, text="/", padx=40, pady=20, command=calc_divide)

button_1 = Button(root, text="1", padx=45, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=45, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=42, pady=20, command=lambda: button_click(3))
button_multiply = Button(root, text="*", padx=40, pady=20, command=calc_multiply)

button_4 = Button(root, text="4", padx=45, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=45, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=42, pady=20, command=lambda: button_click(6))
button_subtract = Button(root, text="-", padx=40, pady=20, command=calc_subtract)

button_7 = Button(root, text="7", padx=45, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=45, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=42, pady=20, command=lambda: button_click(9))
button_add = Button(root, text="+", padx=42, pady=20, command=calc_add)

button_0 = Button(root, text="0", padx=99, pady=20, command=lambda: button_click(0))
button_equal = Button(root, text="=", padx=90, pady=20, command=calc_equal, bg='#00F1FC')

# PUT BUTTONS ON THE SCREEN
button_percent.grid(row=1, column=0)
button_clear.grid(row=1, columnspan=2, column=1)
button_back.grid(row=1, column=3)

button_ofx.grid(row=2, column=0)
button_square.grid(row=2, column=1)
button_square_root.grid(row=2, column=2)
button_divide.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_subtract.grid(row=4, column=3)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_add.grid(row=5, column=3)

button_0.grid(row=6, column=0, columnspan=2)
button_equal.grid(row=6, column=2, columnspan=2)


root.mainloop()