first = input('Введите первое число:')
second = input('Введите второе число:')
third = input('Введите третье число:')
first = float(first)
second = float(second)
third = float(third)
if first == second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')
