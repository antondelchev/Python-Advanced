def create_board(num_of_rows):
    board = []
    for r in range(num_of_rows):
        board.append([])
        for c in range(num_of_rows):
            board[r].append(0)
    return board


def bombs_positions(number_of_bombs):
    positions = []
    for _ in range(number_of_bombs):
        x, y = [el for el in input() if el.isdigit()]
        positions.append((int(x), int(y)))
    return positions


def fill_board(board, positions):
    for el in positions:
        x, y = el
        board[x][y] = "*"

    for r in range(len(board)):
        for c in range(len(board)):
            if not board[r][c] == "*":
                number = 0
                # r
                try:
                    if board[r][c + 1] == "*" and 0 < c + 1 <= len(board) - 1:
                        number += 1
                except IndexError:
                    pass
                try:
                    if board[r][c - 1] == "*" and 0 <= c - 1 <= len(board) - 2:
                        number += 1
                except IndexError:
                    pass
                # r + 1
                try:
                    if board[r + 1][c + 1] == "*" and 0 < r + 1 <= len(board) - 1 and 0 < c + 1 <= len(board) - 1:
                        number += 1
                except IndexError:
                    pass

                try:
                    if board[r + 1][c] == "*" and 0 < r + 1 <= len(board) - 1:
                        number += 1
                except IndexError:
                    pass

                try:
                    if board[r + 1][c - 1] == "*" and 0 < r + 1 <= len(board) - 1 and 0 <= c - 1 <= len(board) - 2:
                        number += 1
                except IndexError:
                    pass
                # r - 1
                try:
                    if board[r - 1][c + 1] == "*" and 0 <= r - 1 < len(board) - 1 and 0 < c + 1 <= len(board) - 1:
                        number += 1
                except IndexError:
                    pass

                try:
                    if board[r - 1][c] == "*" and 0 <= r - 1 < len(board) - 1:
                        number += 1
                except IndexError:
                    pass

                try:
                    if board[r - 1][c - 1] == "*" and 0 <= r - 1 < len(board) - 1 and 0 <= c - 1 <= len(board) - 2:
                        number += 1
                except IndexError:
                    pass

                board[r][c] = number
    return board


n = int(input())
num_of_bombs = int(input())

full_board = (fill_board(create_board(n), bombs_positions(num_of_bombs)))

for element in full_board:
    print(*element)
