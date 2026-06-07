import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.expression = ""
        self.setup_ui()

    def setup_ui(self):

        self.root.geometry("400x500")
        self.root.configure(bg="#1e1e1e")
        self.root.title("Калькулятор")

        self.label = tk.Label(self.root,
                         text="0",
                         font=("Arial", 32),
                         anchor="e",
                         bg="#1e1e1e",
                         fg="#ffffff",
                         width=15
                         )
        self.label.grid(row=0, columnspan=4)

        buttons = [
            ["C", "(", ")", "%"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        for row_ind, row in enumerate(buttons):
            for col_idx, char in enumerate(row):
                cmd = self.calculate if char == '=' else lambda c=char: self.press(c)
                btn = tk.Button(self.root,
                                text=char,
                                font=("Arial", 18),  # шрифт и размер
                                bg="#333333",  # цвет кнопки
                                fg="white",  # цвет текста
                                width=5,  # ширина в символах
                                height=2,  # высота
                                relief="flat",  # стиль границы: flat/raised/sunken/groove
                                borderwidth=0,
                                command=cmd)
                btn.grid(row=row_ind+1, column=col_idx, padx=5, pady=5)


    def press(self, char):
        self.expression += char
        self.label.config(text=self.expression)

    def calculate(self):
        result = eval(self.expression)
        self.label.config(text=result)
        self.expression = str(result)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
