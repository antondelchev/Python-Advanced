data = input()
parentheses_open = []

for index, el in enumerate(data):
    if el == "(":
        parentheses_open.append(index)
    elif el == ")":
        start = parentheses_open.pop()
        print(data[start: index + 1])
