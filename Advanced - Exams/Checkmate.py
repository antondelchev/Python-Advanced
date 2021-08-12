def all_queens(board_input):
    queens = []
    row_num = 0
    for row in board_input:
        for el in row:
            if el == "Q":
                index = row.index(el)
                position = (row_num, index)
                queens.append(position)
        row_num += 1

    return queens


def queens_vs_king_check(board_input, queens_indexes):
    queen_vs_king = []
    for el in queens_indexes:
        queen_row, queen_col = el

        # North
        for r in range(queen_row - 1, -1, -1):
            if board_input[r][queen_col] == "K":
                position = [queen_row, queen_col]
                queen_vs_king.append(position)
                break
            elif board_input[r][queen_col] == "Q":
                break

        # South
        for r in range(queen_row + 1, len(board_input)):
            if board_input[r][queen_col] == "K":
                position = [queen_row, queen_col]
                queen_vs_king.append(position)
                break
            elif board_input[r][queen_col] == "Q":
                break

        # East
        for c in range(queen_col + 1, len(board_input)):
            if board_input[queen_row][c] == "K":
                position = [queen_row, queen_col]
                queen_vs_king.append(position)
                break
            elif board_input[queen_row][c] == "Q":
                break

        # West
        for c in range(queen_col - 1, -1, -1):
            if board_input[queen_row][c] == "K":
                position = [queen_row, queen_col]
                queen_vs_king.append(position)
                break
            elif board_input[queen_row][c] == "Q":
                break

        # North-east
        for r in range(queen_row - 1, len(board_input)):
            for c in range(len(board_input) - r, len(board_input)):
                if board_input[r][r] == "K":
                    position = [queen_row, queen_col]
                    queen_vs_king.append(position)
                    break
                elif board_input[r][r] == "Q":
                    break
                break

        # South-west
        for r in range(queen_row + 1, len(board_input)):
            for c in range(len(board_input) - r - 1):
                if board_input[r][c] == "K":
                    position = [queen_row, queen_col]
                    queen_vs_king.append(position)
                    break
                elif board_input[r][c] == "Q":
                    break
                break

        # North-west
        for r in range(queen_row - 1, -1, -1):
            if board_input[r][r] == "K":
                position = [queen_row, queen_col]
                queen_vs_king.append(position)
                break
            elif board_input[r][r] == "Q":
                break

        # South-east
        for r in range(queen_row + 1, len(board_input)):
            col = queen_col + abs(queen_row - queen_col)
            if col == len(board_input):
                break
            if board_input[r][col] == "K":
                position = [queen_row, queen_col]
                queen_vs_king.append(position)
                break
            elif board_input[r][col] == "Q":
                break

    if not queen_vs_king == []:
        return queen_vs_king
    else:
        return "The king is safe!"


board = []

for n in range(8):
    board.append(input().split())


print(queens_vs_king_check(board, all_queens(board)))
