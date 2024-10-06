my_dict = {'Anton': 1978, 'Dmitry': 1990, 'Victor': 1988, 'Ruslan': 1984, 'Albina': 1977}
print('my_dict: ', my_dict)
print('Существующая запись (Victor): ', my_dict.get('Victor'))
print('Отсутствующая запись: ', my_dict.get('Olga', 'Такой записи нет'))
my_dict.update({'Olga': 1988, 'Oleg': 1994})
print('Обновленный словарь: ', my_dict)
del my_dict['Oleg']
print('Удаленная запись (Oleg)', my_dict)
my_set = {22, 21, 19, 22, 19, 21}
print('Множество my_set', my_set)
my_set.update({17, 48})
print('Множество my_set добавлены две записи ', my_set)
deleted_record = my_set.pop()
print(f'Удалена одна запись ({deleted_record}) из my_set: {my_set}')
