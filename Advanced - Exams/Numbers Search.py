def numbers_searching(*args, info=None):
    if info is None:
        info = []

    full_sequence = [int(el) for el in range(min(args), max(args) + 1)]
    info.append(*[el for el in full_sequence if el not in args])

    duplicates = sorted(set([el for el in args if args.count(el) > 1]))
    info.append(duplicates)

    return info


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
