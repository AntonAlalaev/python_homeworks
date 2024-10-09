class PrimeDefineError(ValueError):
    pass


def is_prime(func):
    def check_prime(num):
        if 4 > num > 0:
            return True
        if num <= 0:
            raise PrimeDefineError("Отрицательные числа и 0 нельзя определить на простые")
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        if check_prime(original_result):
            print("Простое")
        else:
            print("Составное")
        return original_result

    return wrapper


@is_prime
def sum_three(one, two, three):
    return one + two + three


result = sum_three(2, 3, 6)
print(result)
