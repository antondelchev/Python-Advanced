def func_executor(*args):
    all_results = []
    for el in args:
        func_name = el[0].__name__
        x, y = el[1]
        result = globals()[func_name](x, y)
        all_results.append(result)
    return all_results


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
