immutable_var = ('Перечень', [1, 2, 3, 4, 5], 95.5, False)
print(immutable_var)
print(immutable_var[1])
# immutable_var[0] = 'Нет' - ошибка нельзя менять кортеж
immutable_var[1].append(6)  # - можно менять т.к. это элемент входящего в кортеж списка
print(immutable_var)
mutable_list = ['Перечень', [1, 2, 3, 4, 5], 95.5, False]
print(mutable_list)
mutable_list[0] = 'Нет'
print(mutable_list)
