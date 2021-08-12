def board_info():
    board = []
    for _ in range(7):
        board.append(input().split())

    return board


def target_check(player_one, player_two):
    current_board = board_info()

    positions = []
    info = input()

    p1_score = 501
    p2_score = 501

    res = ""

    while info:
        x, y = [el for el in info if el.isdigit()]
        positions.append((int(x), int(y)))
        info = input()

    for index, pos_info in enumerate(positions):
        x, y = pos_info
        if current_board[x][y] == "B":
            if not (index + 1) % 2 == 0:
                res = f"{player_one} won the game with {index + 1} throws!"
            else:
                res = f"{player_two} won the game with {index + 1} throws!"

        elif current_board[x][y].isdigit():
            if not (index + 1) % 2 == 0:
                p1_score -= int(current_board[x][y])
            else:
                p2_score -= int(current_board[x][y])

        elif current_board[x][y] == "D":
            east = int(current_board[x][-1])
            west = int(current_board[x][0])
            north = int(current_board[0][y])
            south = int(current_board[int(len(current_board) - 1)][y])

            points = east + west + north + south

            if not (index + 1) % 2 == 0:
                p1_score -= points * 2
            else:
                p2_score -= points * 2

        elif current_board[x][y] == "T":
            east = int(current_board[x][-1])
            west = int(current_board[x][0])
            north = int(current_board[0][y])
            south = int(current_board[int(len(current_board) - 1)][y])

            points = east + west + north + south

            if not (index + 1) % 2 == 0:
                p1_score -= points * 3
            else:
                p2_score -= points * 3

        if p1_score <= 0:
            res = f"{player_one} won the game with {index + 1 / 2} throws!"
            break
        elif p2_score <= 0:
            res = f"{player_two} won the game with {int((index + 1) / 2)} throws!"
            break

    return res


first_player, second_player = input().split(", ")
print(target_check(first_player, second_player))
