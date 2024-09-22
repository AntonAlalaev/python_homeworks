def divide(first, second):
    """
    Функция осуществляет деление
    в случае деления на 0, возвращает строку Ошибка
    :param first: Делимое
    :param second: Делитель
    :return: Результат деления делимого на делитель
    """
    if float(second) == 0:
        return 'Ошибка'
    return first / second
