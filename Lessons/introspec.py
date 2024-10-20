import pprint

def introspection_info(obj):
    # Возвращаемый словарь
    result = {}

    # Типы объекта
    result["Тип"] = type(obj)

    # Атрибуты объекта
    try:
        result["Атрибуты"] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    except:
        result["Атрибуты"] = "Не имеет атрибутов"

    # Методы объекта.
    try:
        result["Методы"] = [method for method in dir(obj) if callable(getattr(obj, method))]
    except:
        result["Методы"] = "Не имеет методов"

    # Модуль, к которому объект принадлежит.
    try:
        result["Модуль"] = obj.__module__
    except:
        result["Module"] = "Не имеет модуля"

    # Другие интересные свойства объекта, учитывая его тип (для примера длина размер списка или длина строки)
    if isinstance(obj, list):
        result["Размер"] = len(obj)
    elif isinstance(obj, str):
        result["Длина"] = len(obj)

    return result

number_info = introspection_info(42)
pprint.pprint(number_info)