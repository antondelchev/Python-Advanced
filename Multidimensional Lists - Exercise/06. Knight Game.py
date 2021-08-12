def calculations(board_list):
    counter = 0

    for row in range(len(board_list)):
        for col in range(len(board_list[row])):
            if matrix[row][col] == "K":
                try:
                    target = board_list[row + 1][col + 2]
                    if target == "K" and 0 <= row + 1 < len(board_list) and 0 <= col + 2 < len(board_list[row]):
                        counter += 1
                        matrix[row][col] = "0"
                        continue
                except IndexError:
                    pass

                try:
                    target = board_list[row + 2][col + 1]
                    if target == "K" and 0 <= row + 2 < len(board_list) and 0 <= col + 1 < len(board_list[row]):
                        counter += 1
                        matrix[row][col] = "0"
                        continue
                except IndexError:
                    pass

                try:
                    target = board_list[row + 2][col - 1]
                    if target == "K" and 0 <= row + 2 < len(board_list) and 0 <= col - 1 < len(board_list[row]):
                        counter += 1
                        matrix[row][col] = "0"
                        continue
                except IndexError:
                    pass

                try:
                    target = board_list[row + 1][col - 2]
                    if target == "K" and 0 <= row + 1 < len(board_list) and 0 <= col - 2 < len(board_list[row]):
                        counter += 1
                        matrix[row][col] = "0"
                        continue
                except IndexError:
                    pass

                try:
                    target = board_list[row - 1][col - 2]
                    if target == "K" and 0 <= row - 1 < len(board_list) and 0 <= col - 2 < len(board_list[row]):
                        counter += 1
                        matrix[row][col] = "0"
                        continue
                except IndexError:
                    pass

                try:
                    target = board_list[row - 2][col - 1]
                    if target == "K" and 0 <= row - 2 < len(board_list) and 0 <= col - 1 < len(board_list[row]):
                        counter += 1
                        matrix[row][col] = "0"
                        continue
                except IndexError:
                    pass

                try:
                    target = board_list[row - 2][col + 1]
                    if target == "K" and 0 <= row - 2 < len(board_list) and 0 <= col + 1 < len(board_list[row]):
                        counter += 1
                        matrix[row][col] = "0"
                        continue
                except IndexError:
                    pass

                try:
                    target = board_list[row - 1][col + 2]
                    if target == "K" and 0 <= row - 1 < len(board_list) and 0 <= col + 2 < len(board_list[row]):
                        counter += 1
                        matrix[row][col] = "0"
                        continue
                except IndexError:
                    pass

    return counter


n = int(input())
matrix = []

for position in range(n):
    matrix.append(list(input()))

print(calculations(matrix))
