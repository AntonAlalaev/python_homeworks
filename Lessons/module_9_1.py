
def apply_all_func(list_int, *functions):
    results = {}
    for item_function in functions:
        results[str(item_function.__name__)] = item_function(list_int)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))