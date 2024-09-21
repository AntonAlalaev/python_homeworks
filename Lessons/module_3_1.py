calls = 0

# Функция подсчитывает количество вызовов
def count_calls():
    global calls
    calls += 1

# принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(str_in):
    str_len = len(str_in)
    str_up = str.upper(str_in)
    str_down = str.lower(str_in)
    count_calls()
    return str_len, str_up, str_down

# принимает два аргумента: строку и список, и возвращает
# True, если строка находится в этом списке,
# False - если отсутствует
# Регистром строки при проверке пренебречь
def is_contains(string, list_to_search):
    count_calls()
    for item in list_to_search:
        if str.lower(string) == str.lower(item):
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)