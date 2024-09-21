# Функция возвращает произведение цифр числа number
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0]) # получаем первый символ
    if first==0: # Проверим исключение, если число заканчивается на 0
        first=1
    if len(str_number) > 1: # при котором существует вызов рекурсии
        # вызываем функцию рекурсивно
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first # выход из рекурсии


# Основной код программы
result = get_multiplied_digits(420)
print(result)
