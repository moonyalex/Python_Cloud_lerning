import tkinter as tk
# подключаем библиотеку tkinter, называем её tk для краткости

expression = ""  # текущая строка на дисплее

def press(char):
    global expression
    expression += char          # добавляем символ
    label.config(text=expression)  # обновляем дисплей

def calculate():
    global expression
    result = eval(expression)   # Python считает строку как формулу
    label.config(text=result)
    expression = str(result)    # результат становится новым началом

root = tk.Tk()
# создаём главное окно — основной контейнер
# всё остальное будет жить внутри root

root.title("Калькулятор")
# устанавливаем текст в заголовке окна

def say_hello():
    print("Hello!")


label = tk.Label(root, text="Привет!")
# Label — просто текст на экране
# root — в каком окне размещаем
# text — что показывать

button = tk.Button(root, text="Нажми", command=say_hello)
# Button — кнопка
# command= — что вызвать при нажатии
# say_hello БЕЗ скобок — передаём саму функцию, не вызываем её

label.pack()
button.pack()
# pack() — размещает элемент в окне
# без этого виджет создан но невидим

root.mainloop()
# запускает бесконечный цикл обработки событий
# программа "живёт" здесь — ждёт нажатий, движений мыши
# всё что после — выполнится только когда окно закроется