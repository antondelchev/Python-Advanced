def board(number):
    matrix = []

    for _ in range(number):
        matrix.append(list(input()))

    return matrix


def play(commands_count, text, board_ready):
    position = (0, 0)

    for r in range(len(board_ready)):
        done = False
        for c in range(len(board_ready)):
            if board_ready[r][c] == "P":
                position = (r, c)
                done = True
                break
        if done:
            break

    while not commands_count == 0:
        command = input()
        if command == "up":
            if position[0] - 1 < 0:
                if text:
                    text = text[:-1]
            elif board_ready[position[0] - 1][position[1]].isalpha():
                text += board_ready[position[0] - 1][position[1]]
                board_ready[position[0] - 1][position[1]] = "P"
                board_ready[position[0]][position[1]] = "-"

                position = (position[0] - 1, position[1])

            elif board_ready[position[0] - 1][position[1]] == "-":
                board_ready[position[0] - 1][position[1]] = "P"
                board_ready[position[0]][position[1]] = "-"

                position = (position[0] - 1, position[1])

        elif command == "down":
            if position[0] + 1 >= len(board_ready):
                if text:
                    text = text[:-1]
            elif board_ready[position[0] + 1][position[1]].isalpha():
                text += board_ready[position[0] + 1][position[1]]
                board_ready[position[0] + 1][position[1]] = "P"
                board_ready[position[0]][position[1]] = "-"

                position = (position[0] + 1, position[1])

            elif board_ready[position[0] + 1][position[1]] == "-":
                board_ready[position[0] + 1][position[1]] = "P"
                board_ready[position[0]][position[1]] = "-"

                position = (position[0] + 1, position[1])

        elif command == "left":
            if position[1] - 1 < 0:
                if text:
                    text = text[:-1]
            elif board_ready[position[0]][position[1] - 1].isalpha():
                text += board_ready[position[0]][position[1] - 1]
                board_ready[position[0]][position[1] - 1] = "P"
                board_ready[position[0]][position[1]] = "-"

                position = (position[0], position[1] - 1)

            elif board_ready[position[0]][position[1] - 1] == "-":
                board_ready[position[0]][position[1] - 1] = "P"
                board_ready[position[0]][position[1]] = "-"

                position = (position[0], position[1] - 1)

        elif command == "right":
            if position[1] + 1 >= len(board_ready):
                if text:
                    text = text[:-1]
            elif board_ready[position[0]][position[1] + 1].isalpha():
                text += board_ready[position[0]][position[1] + 1]
                board_ready[position[0]][position[1] + 1] = "P"
                board_ready[position[0]][position[1]] = "-"

                position = (position[0], position[1] + 1)

            elif board_ready[position[0]][position[1] + 1] == "-":
                board_ready[position[0]][position[1] + 1] = "P"
                board_ready[position[0]][position[1]] = "-"

                position = (position[0], position[1] + 1)

        commands_count -= 1

    [print("".join(el)) for el in board_ready]
    return text


starting_text = input()
n = int(input())
board_load = board(n)
num_of_commands = int(input())
print(play(num_of_commands, starting_text, board_load))
