import math


def field(number):
    matrix = []

    for _ in range(number):
        matrix.append(input().split())

    return matrix


def play():
    board_ready = field(n)

    position = (0, 0)

    for r in range(len(board_ready)):
        found = False
        for c in range(len(board_ready)):
            if board_ready[r][c] == "P":
                position = (r, c)
                found = True
                break
        if found:
            break

    command = input()
    trace_path = []
    coins = 0
    obstacle = False

    while coins <= 100 and obstacle is False:

        if command == "up":
            if position[0] - 1 < 0 or board_ready[position[0] - 1][position[1]] == "X":
                coins = math.floor(coins * 0.5)
                obstacle = True
                break
            elif board_ready[position[0] - 1][position[1]].isdigit():
                coins += int(board_ready[position[0] - 1][position[1]])
                board_ready[position[0] - 1][position[1]] = "P"
                board_ready[position[0]][position[1]] = "-"

                position = (position[0] - 1, position[1])

        elif command == "down":
            if position[0] + 1 >= len(board_ready) or board_ready[position[0] + 1][position[1]] == "X":
                coins = math.floor(coins * 0.5)
                obstacle = True
                break
            elif board_ready[position[0] + 1][position[1]].isdigit():
                coins += int(board_ready[position[0] + 1][position[1]])
                board_ready[position[0] + 1][position[1]] = "P"
                board_ready[position[0]][position[1]] = "-"

                position = (position[0] + 1, position[1])

        elif command == "left":
            if position[1] - 1 < 0 or board_ready[position[0]][position[1] - 1] == "X":
                coins = math.floor(coins * 0.5)
                obstacle = True
                break
            elif board_ready[position[0]][position[1] - 1].isdigit():
                coins += int(board_ready[position[0]][position[1] - 1])
                board_ready[position[0]][position[1] - 1] = "P"
                board_ready[position[0]][position[1]] = "-"

                position = (position[0], position[1] - 1)

        elif command == "right":
            if position[1] + 1 >= len(board_ready) or board_ready[position[0]][position[1] + 1] == "X":
                coins = math.floor(coins * 0.5)
                obstacle = True
                break
            elif board_ready[position[0]][position[1] + 1].isdigit():
                coins += int(board_ready[position[0]][position[1] + 1])
                board_ready[position[0]][position[1] + 1] = "P"
                board_ready[position[0]][position[1]] = "-"

                position = (position[0], position[1] + 1)

        trace_path.append([position[0], position[1]])
        command = input()

    if obstacle:
        print(f"Game over! You've collected {coins} coins.")
        print("Your path:")
        return trace_path
    else:
        print(f"You won! You've collected {coins} coins.")
        print("Your path:")
        return trace_path


n = int(input())
print(play())
