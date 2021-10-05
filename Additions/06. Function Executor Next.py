def func_executor(*args):
    all_results = []
    for name, numbers in args:
        result = name(*numbers)
        all_results.append(result)
    return all_results


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
