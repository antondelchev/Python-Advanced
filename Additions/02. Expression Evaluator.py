from collections import deque

expression = input().split()

numbers = deque()

math_expressions = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}

for el in expression:
    if el in math_expressions:
        action = math_expressions[el]
        result = numbers.popleft()
        while numbers:
            next_num = numbers.popleft()
            result = action(result, next_num)
        numbers.append(result)

    else:
        numbers.append(int(el))

print(*numbers)
