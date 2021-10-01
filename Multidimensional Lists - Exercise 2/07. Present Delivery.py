# import sys
# from io import StringIO


def is_outside(matrix_row, matrix_col, size):
    if matrix_row < 0 or matrix_col < 0 or matrix_row >= size or matrix_col >= size:
        return True
    return False


# text = """5
# 4
# - X V -
# - S - V
# - - - -
# X - - -
# up
# right
# down
# right
# Christmas morning
# """
#
# text_2 = """3
# 4
# - - - -
# V - X -
# - V C V
# - - - S
# left
# up
# """
#
# sys.stdin = StringIO(text)
# sys.stdin = StringIO(text_2)

num_of_presents = int(input())
size_of_neighbourhood = int(input())

matrix = []

for row in range(size_of_neighbourhood):
    matrix.append(input().split())

santa_row, santa_col = 0, 0
nice_kids = 0
nice_kids_with_gifts = 0

for row in range(size_of_neighbourhood):
    for col in range(size_of_neighbourhood):
        if matrix[row][col] == "S":
            santa_row, santa_col = row, col
        elif matrix[row][col] == "V":
            nice_kids += 1

directions = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "left": lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1),
}

while num_of_presents > 0:
    command = input()

    if command == "Christmas morning":
        break
    matrix[santa_row][santa_col] = "-"
    santa_row, santa_col = directions[command](santa_row, santa_col)
    if is_outside(santa_row, santa_col, size_of_neighbourhood):
        break

    if matrix[santa_row][santa_col] == "X":
        matrix[santa_row][santa_col] = "S"
    elif matrix[santa_row][santa_col] == "V":
        num_of_presents -= 1
        nice_kids -= 1
        nice_kids_with_gifts += 1
        matrix[santa_row][santa_col] = "S"
    elif matrix[santa_row][santa_col] == "C":
        matrix[santa_row][santa_col] = "S"
        for direction, coordinates in directions.items():
            next_r, next_c = directions[direction](santa_row, santa_col)
            if is_outside(next_r, next_c, size_of_neighbourhood):
                continue

            if matrix[next_r][next_c] == "V":
                num_of_presents -= 1
                nice_kids -= 1
                nice_kids_with_gifts += 1
                matrix[next_r][next_c] = "-"
            elif matrix[next_r][next_c] == "X":
                num_of_presents -= 1
                matrix[next_r][next_c] = "-"

if num_of_presents == 0 and nice_kids > 0:
    print("Santa ran out of presents!")

for el in matrix:
    print(*el)

if nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_with_gifts} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
