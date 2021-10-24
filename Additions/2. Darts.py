import sys
from io import StringIO


def is_outside(matrix, r, c):
    return r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix)


data = """Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(3, 3)
"""

data_2 = """George, Hristo
17 8 21 6 13 3 24
16 D D D D D 14
7 D T T T D 15
23 D T B T D 2
9 D T T T D 22
19 D D D D D 10
12 18 4 20 5 11 1
(1, 0)
(2, 3)
(0, 0)
(4, 2)
(5, 1)
(3, 1)
(0, 0)
(2, 3)
"""

sys.stdin = StringIO(data_2)

p1, p2 = input().split(", ")
board = []

p1_score = 501
p2_score = 501

p1_count = 0
p2_count = 0

whose_turn = 1

for _ in range(7):
    board.append(input().split())

while True:
    raw_coordinates = input()[1:-1]
    row, col = map(int, raw_coordinates.split(", "))
    points = 0

    if not is_outside(board, row, col):
        if board[row][col] == "B" and whose_turn % 2 == 1:
            print(f"{p1} won the game with {p1_count + 1} throws!")
            break
        elif board[row][col] == "B" and whose_turn % 2 == 0:
            print(f"{p2} won the game with {p2_count + 1} throws!")
            break
        elif board[row][col].isdigit():
            points += int(board[row][col])
        elif board[row][col] == "D":
            total_sum = int(board[row][0]) + int(board[row][-1]) + int(board[0][col]) + int(board[-1][col])
            points += total_sum * 2
        elif board[row][col] == "T":
            total_sum = int(board[row][0]) + int(board[row][-1]) + int(board[0][col]) + int(board[-1][col])
            points += total_sum * 3

    if whose_turn % 2 == 1:
        p1_count += 1
        p1_score -= points
    else:
        p2_count += 1
        p2_score -= points

    whose_turn += 1

    if p1_score <= 0:
        print(f"{p1} won the game with {p1_count} throws!")
        break
    elif p2_score <= 0:
        print(f"{p2} won the game with {p2_count} throws!")
        break
