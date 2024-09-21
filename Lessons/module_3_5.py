# Функция возвращает произведение цифр числа number
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0]) # получаем первый символ
    if len(str_number) > 1: # при котором существует вызов рекурсии
        # вызываем функцию рекурсивно
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first # выход из рекурсии


# Основной код программы
result = get_multiplied_digits(40203)
print(result)
