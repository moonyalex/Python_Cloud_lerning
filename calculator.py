import tkinter as tk

expression = ""

def press(char):
    global expression
    expression += char
    label.config(text=expression)

def calculate():
    global expression
    result = eval(expression)
    label.config(text=result)
    expression = str(result)

root = tk.Tk()

root.title("Калькулятор")

label = tk.Label(root, text="0")
label.grid(row=0,columnspan=4)

button0 = tk.Button(root, text="0", command=lambda: press("0"))
button_point = tk.Button(root, text=".", command=lambda: press("."))
button_equals = tk.Button(root, text="=", command=calculate)
button_plus = tk.Button(root, text="+", command=lambda: press("+"))
button1 = tk.Button(root, text="1", command=lambda: press("1"))
button2 = tk.Button(root, text="2", command=lambda: press("2"))
button3 = tk.Button(root, text="3", command=lambda: press("3"))
button_minus = tk.Button(root, text="-", command=lambda: press("-"))
button4 = tk.Button(root, text="4", command=lambda: press("4"))
button5 = tk.Button(root, text="5", command=lambda: press("5"))
button6 = tk.Button(root, text="6", command=lambda: press("6"))
button_multiply = tk.Button(root, text="*", command=lambda: press("*"))
button7 = tk.Button(root, text="7", command=lambda: press("7"))
button8 = tk.Button(root, text="8", command=lambda: press("8"))
button9 = tk.Button(root, text="9", command=lambda: press("9"))
button_divide = tk.Button(root, text="/", command=lambda: press("/"))

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button_minus.grid(row=3, column=3)
button0.grid(row=4, column=0)
button_point.grid(row=4, column=1)
button_equals.grid(row=4, column=2)
button_plus.grid(row=4, column=3)


root.mainloop()
