# import sys
# from io import StringIO


def is_outside(matrix_row, matrix_col, size):
    if matrix_row < 0 or matrix_col < 0 or matrix_row >= size or matrix_col >= size:
        return True
    return False


# text = """. . . . .
# x . . . .
# . A . . .
# . . . x .
# . x . . x
# 3
# shoot down
# move right 4
# move left 1
# """
#
# text_2 = """. . . . .
# . . . . .
# . A x . .
# . . . . .
# . x . . .
# 2
# shoot down
# shoot right
# """
#
# sys.stdin = StringIO(text)
# sys.stdin = StringIO(text_2)

matrix = []
current_row, current_col = 0, 0

for _ in range(5):
    matrix.append(input().split())

for row in range(5):
    found = False
    for col in range(5):
        if matrix[row][col] == "A":
            current_row, current_col = row, col
            found = True
            break
    if found:
        break

n = int(input())
targets_hit = []
target_count = 0

for r in range(5):
    for c in range(5):
        if matrix[r][c] == "x":
            target_count += 1

directions_move = {
    "up": lambda x, y, z: (x - z, y),
    "down": lambda x, y, z: (x + z, y),
    "left": lambda x, y, z: (x, y - z),
    "right": lambda x, y, z: (x, y + z),
}

directions_shoot = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "left": lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1),
}

for _ in range(n):
    command_args = input().split()
    order, direction = command_args[0], command_args[1]
    done = False
    if order == "move":
        steps_count = int(command_args[2])
        new_row, new_col = directions_move[direction](current_row, current_col, steps_count)
        if not is_outside(new_row, new_col, 5):
            if matrix[new_row][new_col] == ".":
                matrix[current_row][current_col] = "."
                current_row, current_col = new_row, new_col
                matrix[current_row][current_col] = "A"
    elif order == "shoot":
        shoot_row, shoot_col = directions_shoot[direction](current_row, current_col)
        while not is_outside(shoot_row, shoot_col, 5):
            if matrix[shoot_row][shoot_col] == ".":
                shoot_row, shoot_col = directions_shoot[direction](shoot_row, shoot_col)
                continue
            if matrix[shoot_row][shoot_col] == "x":
                targets_hit.append([shoot_row, shoot_col])
                matrix[shoot_row][shoot_col] = "."
                if len(targets_hit) == target_count:
                    done = True
                break
        if done:
            break

if len(targets_hit) < target_count:
    print(f"Training not completed! {target_count - len(targets_hit)} targets left.")
else:
    print(f"Training completed! All {target_count} targets hit.")

for el in targets_hit:
    print(el)
