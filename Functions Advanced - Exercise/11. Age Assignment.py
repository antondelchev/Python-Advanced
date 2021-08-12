def age_assignment(*args, **kwargs):
    result = {el: 0 for el in args}

    for k, v in result.items():
        for k_sub, v_sub in kwargs.items():
            if k_sub in k:
                result[k] = v_sub

    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
