from collections import deque


def best_list_pureness(input_list, k, max_pureness=0, rotate_num=0, info=""):
    if rotate_num > k:
        maximum, rotation = info.split("-")
        return f"Best pureness {maximum} after {rotation} rotations"

    input_list = deque(input_list)
    current_pureness = sum([index * el for index, el in enumerate(input_list)])
    if current_pureness > max_pureness:
        max_pureness = current_pureness
        info = f"{max_pureness}-{rotate_num}"

    input_list.rotate()
    rotate_num += 1

    return best_list_pureness(input_list, k, max_pureness, rotate_num, info)


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
