# Функция проверки — простое число или нет
# Если число простое, то возвращает True, если нет, то False.
def check_prime(num):
    if num<3:
        print("Ошибка !!! Число меньше 3")
        exit(1)
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

# Функция определяющая пары слагаемых
# На вход должно поступать число больше 1
def get_terms(num):
    numbers=[]
    if num <2:
        print("Ошибка!!! Невозможно определить слагаемые меньше 2")
        exit(1)
    limit=1
    if check_prime(num):
        limit = num//2+1
    else:
        limit = num//2
    for i in range(1,limit):
         numbers.append(i)
         numbers.append(num-i)
    return numbers

# Функция возвращает множители, за исключением 2
def get_multiplier(num):
    if check_prime(num):
        print("Ошибка число простое!!!")
        exit(1)
    multipliers = []
    for i in range(2,num):
        if num%i == 0:
            if i !=2:
                multipliers.append(i)
    return  multipliers

# Основной код программы

for i in range(3,21):
    # Определяем простое число или нет
    # Если простое, то выводим только слагаемые
    # Если нет, то сначала находим множители и раскладываем их на 1+
    if check_prime(i):
        print(i,'-',*get_terms(i))
    else:
        slag=[]
        m = get_multiplier(i)
        if len(m)>0:
            for j in m:
                slag.append(1)
                slag.append(j-1)
            print(i,'-',*slag,*get_terms(i))

