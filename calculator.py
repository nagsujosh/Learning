import math
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Calculator")
root.iconbitmap('icon.ico')
e = Entry(root, width=25, borderwidth=5, state=DISABLED)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20)
e.configure(font=("Times New Roman", 20))

root.maxsize(400, 487)
root.minsize(400, 487)

# root.geometry("380x600")

state_count = 1
variable = ""
answer = 0


# Functions


def is_empty():
    global e
    if e.get():
        pass
        return True
    else:
        e.insert(0, "ERROR")


def ButtonC():
    global e
    global variable
    e.delete(0, END)
    variable = ""


def refresh():
    global e
    string = str(e.get())
    string1 = "123456789.0"
    for i in string:
        if i not in string1:
            string = string.replace(i, "")

    e.delete(0, END)
    e.insert(0, string)


def button_click(number):
    refresh()
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def inverse():
    refresh()
    if is_empty():
        num = float(e.get())
        e.delete(0, END)
        e.insert(0, 1 / num)


def square():
    refresh()
    if is_empty():
        num = float(e.get())
        e.delete(0, END)
        e.insert(0, num ** 2)


def square_root():
    refresh()
    if is_empty():
        num = float(e.get())
        e.delete(0, END)
        e.insert(0, num ** .5)


def OnOff(sc):
    refresh()
    if sc % 2 == 0:
        increase1()
    else:
        increase2()


def increase1():
    global state_count
    global e
    global variable
    e = Entry(root, width=25, borderwidth=5, state=DISABLED)
    e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20)
    e.configure(font=("Times New Roman", 20))
    state_count += 1
    variable = ""


def increase2():
    global state_count
    global e
    global variable
    e = Entry(root, width=25, borderwidth=5)
    e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20)
    e.configure(font=("Times New Roman", 20))
    state_count += 1
    variable = ""


def percentage():
    refresh()
    if is_empty():
        num = float(e.get())
        e.delete(0, END)
        e.insert(0, num/100)


def doBack():
    refresh()
    num = e.get()
    num = num[0:-1]
    e.delete(0, END)
    e.insert(0, num)


def add():
    global variable
    variable = variable + e.get() + "+"
    e.delete(0, END)


def sub():
    global variable
    variable = variable + e.get() + "-"
    e.delete(0, END)


def mul():
    global variable
    variable = variable + e.get() + "*"
    e.delete(0, END)


def div():
    global variable
    variable = variable + e.get() + "/"
    e.delete(0, END)


def do_log():
    equ()
    global answer
    e.delete(0, END)
    e.insert(0, math.log(answer, 10))


def equ():
    global variable
    global answer
    variable = variable + e.get() + "+"
    e.delete(0, END)
    variable = variable + "0"
    n = len(variable)
    i = 0
    while i < n:
        if variable[i] not in "1234567890." and variable[i + 1] not in "1234567890.":
            e.insert(0, "ERROR")
            return True
        i += 1
    numbers = []
    sign = []
    a = ""
    for i in variable:
        if i not in "+-/*":
            a = a + i

        else:
            numbers.append(float(a))
            a = ""
            sign.append(i)

    sign.pop()
    sign.insert(0, "+")
    count = 0
    answer = 0
    for i in numbers:
        if sign[count] == "+":
            answer = answer + i
        if sign[count] == "-":
            answer = answer - i
        if sign[count] == "*":
            answer = answer * i
        if sign[count] == "/":
            answer = answer / i
        count += 1

    e.delete(0, END)
    e.insert(0, answer)


# Button Declaration
percent_button = Button(root, text="%", padx=40, pady=20, command=percentage)
OnOff_button = Button(root, text="ON/OFF", padx=25, pady=20, command=lambda: OnOff(state_count))
C_button = Button(root, text="C", padx=39, pady=20, command=ButtonC)
back_button = Button(root, text="<", padx=44, pady=20, command=doBack)


inverse_button = Button(root, text="1/x", padx=38, pady=20, command=inverse)
square_button = Button(root, text="x^2", padx=35, pady=20, command=square)
root_button = Button(root, text=" x^(1/2)", padx=22, pady=20, command=square_root)
division = Button(root, text="/", padx=45, pady=20, command=div)

button_7 = Button(root, text="7", padx=43, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=42, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=39, pady=20, command=lambda: button_click(9))
multiplication = Button(root, text="X", padx=44, pady=20, command=mul)

button_4 = Button(root, text="4", padx=43, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=42, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=39, pady=20, command=lambda: button_click(6))
substitution = Button(root, text="-", padx=45, pady=20, command=sub)

button_3 = Button(root, text="3", padx=43, pady=20, command=lambda: button_click(3))
button_2 = Button(root, text="2", padx=42, pady=20, command=lambda: button_click(2))
button_1 = Button(root, text="1", padx=39, pady=20, command=lambda: button_click(1))
addition = Button(root, text="+", padx=44, pady=20, command=add)

log = Button(root, text="log", padx=38, pady=20, command=do_log)
button_0 = Button(root, text="0", padx=42, pady=20, command=lambda: button_click(0))
point = Button(root, text=".", padx=41, pady=20, command=lambda: button_click("."))
equal = Button(root, text="=", padx=44, pady=20, command=equ)

# Button Griding
percent_button.grid(row=1, column=1)
OnOff_button.grid(row=1, column=0)
C_button.grid(row=1, column=2)
back_button.grid(row=1, column=3)

inverse_button.grid(row=2, column=0)
square_button.grid(row=2, column=1)
root_button.grid(row=2, column=2)
division.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
multiplication.grid(row=3, column=3)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
substitution.grid(row=4, column=3)

button_3.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_1.grid(row=5, column=2)
addition.grid(row=5, column=3)

log.grid(row=6, column=0)
button_0.grid(row=6, column=1)
point.grid(row=6, column=2)
equal.grid(row=6, column=3)

root.mainloop()
