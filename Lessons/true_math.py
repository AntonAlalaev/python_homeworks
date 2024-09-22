from math import inf


def divide(first, second):
    """
    Функция осуществляет деление
    в случае деления на 0, возвращает бесконечность
    :param first: Делимое
    :param second: Делитель
    :return: Результат деления делимого на делитель
    """
    if float(second) == 0:
        return inf
    return first / second
