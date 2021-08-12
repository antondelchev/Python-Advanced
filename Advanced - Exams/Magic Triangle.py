def get_magic_triangle(number, triangle=None):
    if triangle is None:
        triangle = []

    for row in range(1, number + 1):
        current_col = []

        for col in range(1, number + 1):

            if col == 1 or col == row:
                current_col.append(1)
            elif 1 < col < row:
                current_col.append(triangle[row - 1 - 1][col - 1 - 1] + triangle[row - 1 - 1][col - 1])

        triangle.append(current_col)

    return triangle


print(get_magic_triangle(5))
