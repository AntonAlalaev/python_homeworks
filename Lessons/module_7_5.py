import os
import time


print(f"Текущая директория: {os.getcwd()}")
directory = "/home/anton/PycharmProjects/python_homeworks/os_test_dir"
# Делаем обход каталога directory
# для каждой директории в дереве top возвращается кортеж из трех элементов
# (dir_path, d_names, f_names)
# dir_path - путь к директории
# d_names - список субдиректорий
# f_names - список файлов в директории

# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
print(f"Обход директории {directory}")
for dir_path, d_names, f_names in os.walk(directory):
    print(dir_path, d_names, f_names)
print("\n")

# Примените os.path.join для формирования полного пути к файлам.
file_names = [] # список с полным путем к файлам
for dir_path, d_names, f_names in os.walk(directory):
    for f in f_names:
        file_names.append(os.path.join(dir_path, f))

# Вывод в консоль
file_names.sort()
for file_name in file_names:
    print(file_name)
print("\n")

# Используйте os.path.getmtime,  и модуль time для получения и отображения времени последнего изменения файла.
for file_name in file_names:
    f_time = os.path.getatime(file_name)
    file_time = time.ctime(f_time)
    print(f"Путь к файлу {file_name}")
    print(f"Время последнего изменения {file_time} ")
print("\n")

# Используйте os.path.getsize для получения размера файла.
for file_name in file_names:
    f_size = os.path.getsize(file_name)
    print(f"Путь к файлу {file_name}")
    print(f"Размер файла {f_size} ")
print("\n")

# Используйте os.path.dirname для получения родительской директории файла.
print(f"Родительская директория для {directory}\n {os.path.dirname(directory)}")
