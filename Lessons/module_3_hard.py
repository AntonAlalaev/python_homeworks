# Функция подсчитывает сумму всех элементов, рекурсивно
# Если строковый элемент, то его длину
def calculate_structure_sum(a):
    suma = 0
    if isinstance(a, list):
        # Рекурсивно суммируем элементы списка
        for i in a:
            suma += calculate_structure_sum(i)
    elif isinstance(a, dict):
        # Для словаря суммируем ключи и значения
        for k, v in a.items():
            suma += calculate_structure_sum(k) + calculate_structure_sum(v)
    elif isinstance(a, tuple):
        # Кортеж, разбираем его по элементам как список
        for j in a:
            suma += calculate_structure_sum(j)
    elif isinstance(a, set):
        # Множество, разбираем его по элементам как список
        for k in a:
            suma += calculate_structure_sum(k)
    elif isinstance(a, (int, float)):
        # Суммируем числа
        suma += a
    elif isinstance(a, str):
        # Для строк суммируем длину
        suma += len(a)
    else:
        print("Неизвестный тип в ", type(a))
    return suma  # Возвращаем итоговую сумму


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
