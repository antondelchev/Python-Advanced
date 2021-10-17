def digital_root(n):
    digits_sum = sum([int(el) for el in str(n)])

    if len(str(digits_sum)) == 1:
        return digits_sum
    return digital_root(digits_sum)
