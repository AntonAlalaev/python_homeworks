class IncorrectVinNumber(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


class IncorrectCarNumbers(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


class Car:

    @staticmethod
    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный VIN", vin_number)
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера", vin_number)
        else:
            return True

    @staticmethod
    def __is_valis_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров", numbers)
        elif len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера", numbers)
        else:
            return True

    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valis_numbers(numbers):
            self.__numbers = numbers


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message, exc.extra_info)
except IncorrectCarNumbers as exc:
    print(exc.message, exc.extra_info)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message, exc.extra_info)
except IncorrectCarNumbers as exc:
    print(exc.message, exc.extra_info)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message, exc.extra_info)
except IncorrectCarNumbers as exc:
    print(exc.message, exc.extra_info)
else:
    print(f'{third.model} успешно создан')
