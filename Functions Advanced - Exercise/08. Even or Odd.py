def even_odd(*args):
    args = list(args)

    if "even" in args:
        args.remove("even")
        res = [el for el in args if el % 2 == 0]
        return res
    elif "odd" in args:
        args.remove("odd")
        res = [el for el in args if not el % 2 == 0]
        return res


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
