def is_valid(target, r1, c1, r2, c2):
    status = True
    for r in range(len(target)):
        if r1 < 0 or r1 > len(target) or c1 < 0 or c1 > len(target[r]) or \
                r2 < 0 or r2 > len(target) or c2 < 0 or c2 > len(target[r]):
            status = False

    return status


rows, cols = [int(el) for el in input().split()]
matrix = []

for row in range(rows):
    matrix.append([el for el in input().split()])

command = input()

while not command == "END":
    info = command.split()
    if len(info) == 5:
        row_a = int(info[1])
        col_a = int(info[2])
        row_b = int(info[3])
        col_b = int(info[4])

        if is_valid(matrix, row_a, col_a, row_b, col_b) and info[0] == "swap":
            matrix[row_a][col_a], matrix[row_b][col_b] = matrix[row_b][col_b], matrix[row_a][col_a]
            for el in matrix:
                print(*el)

        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    command = input()
