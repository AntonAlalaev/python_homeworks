def print_params(a=1, b='Строка', c=True):
    print(a, b, c)


print_params()
print_params(3)
print_params(b='другая строка')
print_params(c=10)
values_list = [54.32, 'Привет', False]
print_params(*values_list)  # распаковывает список и передает каждый параметр
print_params(values_list)  # Передает только первый парамтер в качестве списка
values_dict = {'a': 45, 'b': "Что-то", 'c': False}
print_params(**values_dict) # Распаковывает словарь и передает каждый параметр
print_params(values_dict) # Не распаковываеь и передает словарь в качетсве первого аргумента

values_list2 = [5,5]
print_params(*values_list2,42)