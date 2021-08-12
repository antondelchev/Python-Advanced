r, c = [int(el) for el in input().split()]
matrix = []

result = [[f"{chr(num)}{chr(nested_num)}{chr(num)}" for nested_num in range(num, num + c)] for num in range(97, 97 + r)]

[print(*el) for el in result]
