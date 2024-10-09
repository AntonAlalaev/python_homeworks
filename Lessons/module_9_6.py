def all_variants(text):
    for i in range(len(text)):
        for j in range(i+1, len(text)+1):
            yield text[i:j]

a = all_variants("abc")
for i in a:
    print(i)

# Вывод:
# a ab abc b bc c

# чтобы получился вывод в такой же последовательности как в задании
# функция будет выглядеть примерно так:
# но мне первый вариант больше нравится, он более локаничен

def all_variants2(text):
    for i in range(1, len(text) + 1):
        for j in range(len(text)):
            if i+j <= len(text):
                yield text[j:i+j]

a = all_variants2("abc")
for i in a:
    print(i)

# Вывод:
# a b c ab bc abc