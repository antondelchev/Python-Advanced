def func_executor(*args):
    result = []
    num_of_commands = len(args)
    for i in range(num_of_commands):
        func = args[i][0]
        func_args = args[i][1]
        if func.__name__ == "sum_numbers":
            result.append(sum_numbers(*func_args))
        elif func.__name__ == "multiply_numbers":
            result.append(multiply_numbers(*func_args))

    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
