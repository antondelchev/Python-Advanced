# import sys
# from io import StringIO


def is_inside(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return False
    return matrix[r][c] == "K"


def knight_moves(r, c, size):
    knights_counter = 0
    if is_inside(r - 2, c + 1, size):
        knights_counter += 1
    if is_inside(r - 1, c + 2, size):
        knights_counter += 1
    if is_inside(r + 1, c + 2, size):
        knights_counter += 1
    if is_inside(r + 2, c + 1, size):
        knights_counter += 1
    if is_inside(r + 2, c - 1, size):
        knights_counter += 1
    if is_inside(r + 1, c - 2, size):
        knights_counter += 1
    if is_inside(r - 1, c - 2, size):
        knights_counter += 1
    if is_inside(r - 2, c - 1, size):
        knights_counter += 1
    return knights_counter


# text = """5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0
# """
#
# text_2 = """8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK
# """
#
# sys.stdin = StringIO(text)
# sys.stdin = StringIO(text_2)

n = int(input())

matrix = []

for _ in range(n):
    line = input().split()
    for sub in line:
        matrix.append(list(sub))

strongest = float("-inf")

removed_knights = 0

while True:
    max_targets, knight_row, knight_col = 0, 0, 0
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "0":
                continue
            count_affected = knight_moves(row, col, n)
            if count_affected > max_targets:
                max_targets, knight_row, knight_col = count_affected, row, col
    if max_targets == 0:
        break
    matrix[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)
