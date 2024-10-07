import os
import time


print(f"Текущая директория: {os.getcwd()}")
directory = "."
# Делаем обход каталога directory
# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory

# Примените os.path.join для формирования полного пути к файлам.
file_names = [] # список с полным путем к файлам
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)
        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)
        # Форматируем время
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # Получаем размер файла
        filesize = os.path.getsize(filepath)
        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)
        # Выводим информацию о файле
        print(f'Обнаружен файл: {file},\nПуть: {filepath},\nРазмер: ' + \
                f'{filesize} байт, Время изменения: {formatted_time},\n' + \
                f'Родительская директория: {parent_dir}\n')
