import io


def custom_write(file_name, strings):
    # Словарь для возврата
    str_positions = {}
    with open(file_name, "w", encoding="utf-8") as file:
        # вот с этим циклом пришлось почитать что такое
        # enumerate
        for index, string in enumerate(strings, start=1):
            position = file.tell()
            file.write(string + "\n")
            # запись в словарь
            str_positions[(index, position)] = string
        file.close() # можно и не закрывать
    return str_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
