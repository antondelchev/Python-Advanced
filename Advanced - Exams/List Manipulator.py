import itertools


def list_manipulator(input_list, command, position, *args):
    if command == "add" and position == "beginning":
        return list(itertools.chain(args, input_list))
    elif command == "add" and position == "end":
        return list(itertools.chain(input_list, args))

    elif command == "remove" and position == "beginning":
        try:
            if args:
                del input_list[0: int(*args)]
                return input_list
            else:
                input_list.pop(0)
                return input_list
        except IndexError:
            pass
    elif command == "remove" and position == "end":
        try:
            if args:
                count = int(*args)
                while count > 0:
                    input_list.pop()
                    count -= 1
                return input_list
            else:
                input_list.pop()
                return input_list
        except IndexError:
            pass


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
