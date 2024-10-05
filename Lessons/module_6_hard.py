class Figure:
    sides_count = 0  # Количество сторон

    @staticmethod
    def __is_valid_color(color_set):
        """
        Статический метод, проверяет на корректность набора цвета
        :param color_set: кортеж из трех целых чисел в диапазоне от 0 до 255
        :return: True - в случае если цвет задан корректно, False - если нет
        """
        if len(color_set) == 3:
            color_ok = True
            for index in range(0, len(color_set)):
                if color_set[index] < 0 or color_set[index] > 255:
                    color_ok = False
                    break
            return color_ok
        else:
            return False

    def get_color(self):
        """
        Возвращает текущий цвет класса
        :return:
        """
        return list(self.__color)

    def __set_color(self, color):
        """
        Внутренний метод для установки цвета
        :param color: кортеж
        :return: ничего
        """
        if isinstance(color, tuple):
            if self.__is_valid_color(color):
                self.__color = color
            else:
                print("Цвет определен неверно, установлен по умолчанию")
        else:
            print("Для установки цвета нужен кортеж, цвет установлен по умолчанию")

    def set_color(self, r, g, b):
        """
        Внешний метод для установки цвета
        :param r: интенсивность красного от 0 до 255
        :param g: интенсивность зеленого от 0 до 255
        :param b: интенсивность синего от 0 до 255
        :return: ничего
        """
        self.__set_color((r, g, b))

    def __is_valid_sides(self, sides_list):
        """
        Проверяет на соответствие сторон
        :param sides_list: список сторон
        :return: False или True
        """
        if len(sides_list) == self.sides_count:
            for i in sides_list:
                if not isinstance(i, int) or i < 1:
                    return False
            return True
        else:
            return False

    def set_sides(self, *args):
        """
        Задает значения сторон для фигуры
        :param args: аргументы в виде целых чисел
        :return: ничего
        """
        lst = list(args)
        if self.__is_valid_sides(lst):
            self.__sides = lst
        else:
            if not self.__initialize:
                return
            default_list = []
            for i in range(self.sides_count):
                default_list.append(1)
            self.__sides = default_list

    def get_sides(self):
        return self.__sides

    def __init__(self, *args):
        self.__initialize = True
        self.__sides = []
        self.__color = [255, 255, 255]  # Цвет по умолчанию
        self.filled = True
        self.__set_color(args[0])
        lst = []
        for i in range(1, len(args)):
            lst.append(args[i])
        self.set_sides(*lst)
        self.__initialize = False

    def __len__(self):
        """
        Возвращает периметр фигуры - сумму длин всех сторон
        :return:
        """
        perimetr = 0
        for i in self.__sides:
            perimetr += i
        return perimetr


class Circle(Figure):
    """
    Класс окружности
    """
    sides_count = 1  # Количество сторон

    # Вычисляет радиус окружности по заданной длине
    @property
    def __radius(self):
        return self.__len__() / (3.14159 * 2)

    # Возвращает площадь окружности
    def get_square(self):
        return self.__radius ** 2 * 3.14159


class Triangle(Figure):
    """
    Класс треугольника
    """
    sides_count = 3  # Количество сторон

    # Возвращает площадь треугольника
    def get_square(self):
        half_perimetr = self.__len__() / 2
        s = (half_perimetr - self.get_sides()[0]) * \
            (half_perimetr - self.get_sides()[1]) * \
            (half_perimetr - self.get_sides()[2])
        return (half_perimetr * s) ** 0.5


class Cube(Figure):
    """
    Класс куба
    """
    sides_count = 12

    # Метод переопределен, чтобы на вход подавалась одна сторона
    def set_sides(self, *lst_):
        lst = list(lst_)
        if len(lst) == 1 and isinstance(lst[0], int) and lst[0] > 0:
            new_size = []
            for i in range(0, self.sides_count):
                new_size.append(lst[0])
            super().set_sides(*new_size)  # Вызываем метод родительского класса
        else:
            super().set_sides(*lst)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
