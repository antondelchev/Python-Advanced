rows, cols = [int(el) for el in input().split()]
matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

max_sum = 0
coordinates = None

if rows >= 3 and cols >= 3:
    for row in range(0, rows - 2):
        for col in range(0, cols - 2):
            current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
                          matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                          matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
            if current_sum >= max_sum:
                max_sum = current_sum
                coordinates = (row, col)

if coordinates:
    rows_sub, cols_sub = coordinates
    print(f"Sum = {max_sum}")
    print(f"{matrix[rows_sub][cols_sub]} {matrix[rows_sub][cols_sub + 1]} "
          f"{matrix[rows_sub][cols_sub + 2]}")
    print(f"{matrix[rows_sub + 1][cols_sub]} "
          f"{matrix[rows_sub + 1][cols_sub + 1]} {matrix[rows_sub + 1][cols_sub + 2]}")
    print(f"{matrix[rows_sub + 2][cols_sub]} "
          f"{matrix[rows_sub + 2][cols_sub + 1]} {matrix[rows_sub + 2][cols_sub + 2]}")
