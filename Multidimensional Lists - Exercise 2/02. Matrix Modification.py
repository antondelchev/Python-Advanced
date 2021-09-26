# import sys
# from io import StringIO


def is_invalid(index_row, index_col, size):
    if index_row < 0 or index_col < 0 or index_row >= size or index_col >= size:
        return True
    return False


# text = """3
# 1 2 3
# 4 5 6
# 7 8 9
# END
# """
#
# text_2 = """4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END
# """

# sys.stdin = StringIO(text)
# sys.stdin = StringIO(text_2)

n = int(input())

matrix = []

for _ in range(n):
    int_line = [int(x) for x in input().split()]
    matrix.append(int_line)

while True:
    line = input()
    if line == "END":
        for el in matrix:
            print(*el)
        break

    command, row, col, value = line.split()
    row = int(row)
    col = int(col)
    value = int(value)

    if command == "Add":
        if is_invalid(row, col, n):
            print("Invalid coordinates")
        else:
            matrix[row][col] += value
    elif command == "Subtract":
        if is_invalid(row, col, n):
            print("Invalid coordinates")
        else:
            matrix[row][col] -= value
