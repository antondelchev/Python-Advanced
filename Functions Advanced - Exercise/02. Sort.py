def sorting_asc(*args):
    return sorted(*args)


nums = [int(el) for el in input().split(" ")]

print(sorting_asc(nums))
