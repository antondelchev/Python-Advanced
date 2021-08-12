def hunting_ground(num):
    field = []

    for row in range(num):
        field.append(list(input()))

    return field


def snake_position(board_list):
    position = (0, 0)

    for r in range(len(board_list)):
        found = False
        for c in range(len(board_list)):
            if board_list[r][c] == "S":
                position = (r, c)
                found = True
                break
        if found:
            break

    return position


def play():
    board = hunting_ground(n)
    x, y = snake_position(board)

    out_of_bounds = False
    food = 0
    position = (x, y)

    command = input()
    while command:
        if command == "up":
            if position[0] - 1 < 0:
                board[position[0]][position[1]] = "."
                out_of_bounds = True
            if position[0] - 1 > len(board) - 1:
                out_of_bounds = True
            elif board[position[0] - 1][position[1]] == "-":
                board[position[0] - 1][position[1]] = "S"
                board[position[0]][position[1]] = "."
                position = (position[0] - 1, position[1])
            elif board[position[0] - 1][position[1]] == "*":
                board[position[0] - 1][position[1]] = "S"
                board[position[0]][position[1]] = "."
                position = (position[0] - 1, position[1])
                food += 1
            elif board[position[0] - 1][position[1]] == "B":
                board[position[0]][position[1]] = "."
                board[position[0] - 1][position[1]] = "."
                for r in range(len(board)):
                    done = False
                    for c in range(len(board)):
                        if board[r][c] == "B":
                            board[r][c] = "S"
                            position = (r, c)
                            done = True
                            break
                    if done:
                        break

        elif command == "down":
            if position[0] + 1 > len(board) - 1:
                board[position[0]][position[1]] = "."
                out_of_bounds = True
            elif board[position[0] + 1][position[1]] == "-":
                board[position[0] + 1][position[1]] = "S"
                board[position[0]][position[1]] = "."
                position = (position[0] + 1, position[1])
            elif board[position[0] + 1][position[1]] == "*":
                board[position[0] + 1][position[1]] = "S"
                board[position[0]][position[1]] = "."
                position = (position[0] + 1, position[1])
                food += 1
            elif board[position[0] + 1][position[1]] == "B":
                board[position[0]][position[1]] = "."
                board[position[0] + 1][position[1]] = "."
                for r in range(len(board)):
                    done = False
                    for c in range(len(board)):
                        if board[r][c] == "B":
                            board[r][c] = "S"
                            position = (r, c)
                            done = True
                            break
                    if done:
                        break

        elif command == "left":
            if position[1] - 1 < 0:
                board[position[0]][position[1]] = "."
                out_of_bounds = True
            elif board[position[0]][position[1] - 1] == "-":
                board[position[0]][position[1] - 1] = "S"
                board[position[0]][position[1]] = "."
                position = (position[0], position[1] - 1)
            elif board[position[0]][position[1] - 1] == "*":
                board[position[0]][position[1] - 1] = "S"
                board[position[0]][position[1]] = "."
                position = (position[0], position[1] - 1)
                food += 1
            elif board[position[0]][position[1] - 1] == "B":
                board[position[0]][position[1]] = "."
                board[position[0]][position[1] - 1] = "."
                for r in range(len(board)):
                    done = False
                    for c in range(len(board)):
                        if board[r][c] == "B":
                            board[r][c] = "S"
                            position = (r, c)
                            done = True
                            break
                    if done:
                        break

        elif command == "right":
            if position[1] + 1 > len(board) - 1:
                board[position[0]][position[1]] = "."
                out_of_bounds = True
            elif board[position[0]][position[1] + 1] == "-":
                board[position[0]][position[1] + 1] = "S"
                board[position[0]][position[1]] = "."
                position = (position[0], position[1] + 1)
            elif board[position[0]][position[1] + 1] == "*":
                board[position[0]][position[1] + 1] = "S"
                board[position[0]][position[1]] = "."
                position = (position[0], position[1] + 1)
                food += 1
            elif board[position[0]][position[1] + 1] == "B":
                board[position[0]][position[1]] = "."
                board[position[0]][position[1] + 1] = "."
                for r in range(len(board)):
                    done = False
                    for c in range(len(board)):
                        if board[r][c] == "B":
                            board[r][c] = "S"
                            position = (r, c)
                            done = True
                            break
                    if done:
                        break

        if food == 10 or out_of_bounds is True:
            break
        else:
            command = input()

    if food == 10:
        print("You won! You fed the snake.")
        print(f"Food eaten: {food}")
        [print("".join(el)) for el in board]
        return board
    elif out_of_bounds is True:
        print("Game over!")
        print(f"Food eaten: {food}")
        [print("".join(el)) for el in board]
        return board


n = int(input())
print(play())
