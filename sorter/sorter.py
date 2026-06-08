import os
import shutil

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
    for item in os.listdir(folder_path):
        file_path = os.path.join(folder_path, item) # Используем os.path.join для кроссплатформенности
        if not os.path.isfile(file_path):  # пропускаем папки
            continue
        _, ext = os.path.splitext(item)
        category = get_categories(ext)
        dest_folder = os.path.join(folder_path, category) # Используем os.path.join
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(dest_folder, item)) # Используем os.path.join
    return "Сортировка завершена"


def count_items(folder_path):
    # Получаем список всех элементов в базовой папке
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
        print(f"Всего файлов в папке {item}: {file_count} шт.")
    print(f"Всего файлов в папке {folder_path}: {count_all_items} шт.")


print(sort_folder("D:/need_too_sort"))
count_items("D:/need_too_sort")

