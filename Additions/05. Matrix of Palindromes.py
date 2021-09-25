r, c = [int(x) for x in input().split()]

matrix = []

for row in range(r):
    pattern = []
    for col in range(c):
        pattern.append(f"{chr(97 + row)}{chr(97 + row + col)}{chr(97 + row)}")
    matrix.append(pattern)

for el in matrix:
    print(*el)
