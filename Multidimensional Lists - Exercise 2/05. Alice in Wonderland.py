# import sys
# from io import StringIO


def is_outside(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


# text = """5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left
# """
#
# text_2 = """7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right
# """
#
# sys.stdin = StringIO(text)
# sys.stdin = StringIO(text_2)

n = int(input())

matrix = []

for row in range(n):
    col = input().split()
    matrix.append(col)

alice_row, alice_col = (0, 0)
tea_bags = 0

for row in range(n):
    found = False
    for col in range(n):
        if matrix[row][col] == "A":
            alice_row, alice_col = row, col
            found = True
            break
    if found:
        break

directions = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "left": lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1),
}

matrix[alice_row][alice_col] = "*"
while tea_bags < 10:
    direction = input()
    alice_row, alice_col = directions[direction](alice_row, alice_col)

    if is_outside(alice_row, alice_col, n):
        break

    if matrix[alice_row][alice_col].isdigit():
        tea_bags += int(matrix[alice_row][alice_col])
        matrix[alice_row][alice_col] = "*"
    elif matrix[alice_row][alice_col] == ".":
        matrix[alice_row][alice_col] = "*"
    elif matrix[alice_row][alice_col] == "R":
        matrix[alice_row][alice_col] = "*"
        break

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for el in matrix:
    print(*el)
