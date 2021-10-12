def filter_list(expression):
    ints_only = []
    for el in expression:
        if type(el) == int:
            ints_only.append(el)
    return ints_only
