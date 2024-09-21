# Функция возвращает однокоренные слова, как в ту, так и
# в другую сторону
def single_root_words(root_word, *args):
    res = []
    for item in args:
        if str.lower(root_word) in str.lower(item):
            res.append(item)
        if str.lower(item) in str.lower(root_word):
            res.append(item)
    return res


# Основной код программы
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
