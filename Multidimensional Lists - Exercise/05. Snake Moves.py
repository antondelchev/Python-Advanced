rows, cols = [int(el) for el in input().split()]
string_info = list(input())
matrix = []

for row in range(rows):
    matrix.append([])

position = 0

for row in range(rows):

    if row % 2 == 0:
        string_info = string_info
        if position > len(string_info):
            position = 0
        for col in range(cols):
            matrix[row].append(string_info[position])
            position += 1
            if position > len(string_info) - 1:
                position = 0

    else:
        if position > len(string_info):
            position = 0
        for col in range(cols - 1, -1, -1):
            matrix[row].insert(0, string_info[position])
            position += 1
            if position > len(string_info) - 1:
                position = 0

[print(*el, sep="") for el in matrix]
