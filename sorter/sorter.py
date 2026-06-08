import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

CATEGORIES = {
    "Изображения": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Видео": [".mp4", ".avi", ".mov", ".mkv"],
    "Документы": [".pdf", ".docx", ".txt", ".xlsx"],
    "Код": [".py", ".js", ".html", ".css"],
    "Архивы": [".zip", ".rar", ".7z"],
    "Музыка": [".mp3", ".flac", ".waw", ".aac", ".ogg"],
}


def get_categories(type_file):
    for category, extension in CATEGORIES.items():
        if type_file in extension:
            return category
    return "Разное"


def sort_folder(folder_path):
    if not os.path.isdir(folder_path):
        return "Ошибка: Указанная папка не существует!"
    # Получаем список всех элементов в указанной директории
    for item in os.listdir(folder_path):
        file_path = os.path.join(folder_path, item)  # Используем os.path.join для кроссплатформенности
        if not os.path.isfile(file_path):  # пропускаем папки
            continue
        _, ext = os.path.splitext(item)
        category = get_categories(ext)
        dest_folder = os.path.join(folder_path, category)  # Используем os.path.join
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(dest_folder, item))  # Используем os.path.join
    return "Сортировка завершена"


def count_items(folder_path):
    # Получаем список всех элементов в базовой папке
    results = []
    items_in_folder = os.listdir(folder_path)
    count_all_items = 0
    for item in items_in_folder:
        item_path = os.path.join(folder_path, item)

        # Проверяем, является ли элемент папкой (т.е. папкой-категорией)
        if os.path.isdir(item_path):

            file_count = 0
            # Итерируем по содержимому папки категории
            for file_in_category in os.listdir(item_path):
                full_file_path = os.path.join(item_path, file_in_category)
                # Считаем только файлы, игнорируя возможные подпапки (хотя sort_folder их не создает)
                if os.path.isfile(full_file_path):
                    file_count += 1
            count_all_items += file_count
            results.append(f"Всего файлов в папке {item}: {file_count} шт.")
    if not results:
        return "В указанной папке нет категорий для сортировки."
    return "\n".join(results)


def browse_folder():
    folder_input = filedialog.askdirectory()
    if folder_input:
        entry_folder_path.delete(0, tk.END)
        entry_folder_path.insert(0, folder_input)

def start_sorting():
    folder_path = entry_folder_path.get()

    if not folder_path:
        messagebox.showwarning("Предупреждение","Пожалуйста, введите путь к папке")
        return

    sort_message = sort_folder(folder_path)
    if sort_message.startswith("Ошибка"):
        messagebox.showinfo("Ошибка сортировки", sort_message)
        return
    else:
        messagebox.showinfo("Сортировка", sort_message)

    count_results = count_items(folder_path)

    results_text.config(state=tk.NORMAL)
    results_text.delete(1.0, tk.END)
    results_text.insert(tk.END, count_results)
    results_text.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Сортировщик файлов")
root.geometry("500x400")

frame_path = tk.Frame(root)
frame_path.pack(pady=10)

label_path = tk.Label(frame_path, text="Путь к папке:")
label_path.pack(side=tk.LEFT, padx=5)

entry_folder_path = tk.Entry(frame_path, width=50)
entry_folder_path.pack(side=tk.LEFT, padx=5)

button_browse = tk.Button(frame_path, text="Обзор...", command=browse_folder)
button_browse.pack(side=tk.LEFT, padx=5)

button_sort = tk.Button(frame_path, text="Начать сортировку и подсчет", command=start_sorting)
button_sort.pack(side=tk.LEFT, padx=5)

results_text = tk.Text(root, width=60, height=10, state=tk.NORMAL)
results_text.pack(pady=10)

root.mainloop()


