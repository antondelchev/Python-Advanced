# import sys
# from io import StringIO


def is_outside(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


# text = """5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0
# """
#
# text_2 = """8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22
# """
#
# sys.stdin = StringIO(text)
# sys.stdin = StringIO(text_2)

n = int(input())

matrix = []
bunny_location = (0, 0)

for row in range(n):
    matrix.append(input().split())
    current_row = matrix[row]
    for index, el in enumerate(current_row):
        if el == "B":
            bunny_location = (row, index)

directions = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "left": lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1),
}

best_direction = ""
direction_coordinates = []
eggs_collected = 0

for direction, step in directions.items():
    current_row, current_col = bunny_location
    eggs = 0
    path = []
    while True:
        current_row, current_col = step(current_row, current_col)
        if is_outside(current_row, current_col, n):
            break
        if matrix[current_row][current_col] == "X":
            break

        eggs += int(matrix[current_row][current_col])
        path.append([current_row, current_col])
    if eggs >= eggs_collected:
        best_direction = direction
        direction_coordinates = path
        eggs_collected = eggs

print(best_direction)
for step in direction_coordinates:
    print(step)
print(eggs_collected)
