import sys
from io import StringIO


def is_outside(matrix, r, c):
    return r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix)


data = """B 30 14 23 20 24
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)
"""

sys.stdin = StringIO(data)

board = []
coordinates = set()
total_points = 0

for _ in range(6):
    board.append(input().split())

for _ in range(3):
    raw_coordinates = input()[1:-1]
    row, col = raw_coordinates.split(", ")
    coordinates.add((row, col))

for el in coordinates:
    row, col = map(int, el)
    if is_outside(board, row, col):
        continue

    current_points = 0
    if board[row][col] == "B":
        for position in range(0, 6):
            if board[position][col].isdigit():
                current_points += int(board[position][col])

    total_points += current_points

if 0 <= total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
elif 100 <= total_points <= 199:
    prize = "Football"
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
elif 200 <= total_points <= 299:
    prize = "Teddy Bear"
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
elif total_points >= 300:
    prize = "Lego Construction Set"
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
