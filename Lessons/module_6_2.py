class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white', 'metallic']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self._model = model
        self._engine_power = engine_power
        if str(color).lower() in self.__COLOR_VARIANTS:
            self._color = color
        # Тоже добавил немного отсебятины для проверки цветов в конструкторе
        else:
            print("Такого цвета нет в списке допустимых цветов. Выбран цвет по умолчанию.")
            self._color = self.__COLOR_VARIANTS[0]

    def get_model(self):
        return self._model

    def get_horsepower(self):
        return self._engine_power

    def get_color(self):
        return self._color

    def print_info(self):
        print(f"Модель: {self._model}")
        print(f"Мощность двигателя: {self._engine_power}")
        print(f"Цвет: {self._color}")
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if str(new_color).lower() not in self.__COLOR_VARIANTS:
            print(f"Нельзя сменить цвет на {new_color}")
        else:
            self._color = new_color


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, engine_power, color)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
