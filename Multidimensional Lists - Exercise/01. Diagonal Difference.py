size_of_matrix = int(input())
matrix = []

primary_diagonal = 0
secondary_diagonal = 0

for row in range(size_of_matrix):
    matrix.append([int(el) for el in input().split()])
    primary_diagonal += matrix[row][row]

for row in range(size_of_matrix):
    for col in range(size_of_matrix - 1, -1, -1):
        if col == size_of_matrix - 1 - row:
            secondary_diagonal += matrix[row][col]

print(abs(primary_diagonal - secondary_diagonal))
