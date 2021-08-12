def even_nums(*args):
    nums_int = [int(el) for el in args]
    res = [el for el in nums_int if el % 2 == 0]
    return res


nums = input().split(" ")

result = (list(filter(even_nums, nums)))
print([int(el) for el in result])
