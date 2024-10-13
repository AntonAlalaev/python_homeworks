from datetime import datetime
import multiprocessing

def read_info(file_name):
    all_data=[]
    with open(file_name, "r") as file:
        for _ in file:
            all_data.append(file.readline())
    print(f"Файл {file_name} прочитан")

if __name__ == "__main__":
    # Создаем список файлов
    files = []
    for i in range(1,5):
        files.append(f"file {i}.txt")

    start_time = datetime.now()
    # Cчитываем файлы линейно
    for item in files:
        read_info(item)
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Время линейного считывания файлов {total_time}")

    start_time = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)

    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Время много процессного считывания файлов {total_time}")
