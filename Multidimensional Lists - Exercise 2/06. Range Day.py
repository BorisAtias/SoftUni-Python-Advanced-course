"""rows, cols = 5, 5
matrix = [[x for x in input().split()] for _ in range(5)]


def are_targets_left(my_matrix):
    is_found = 0
    for row in range(len(my_matrix)):
        for col in range(len(my_matrix)):
            if my_matrix[row][col] == "x":
                is_found += 1

    return is_found


def find_shooter(my_matrix):
    for row in range(len(my_matrix)):
        for col in range(len(my_matrix[row])):
            if my_matrix[row][col] == "A":
                return (row, col)


def move_shooter(shooter_position, direction, steps, my_matrix):
    row, col = shooter_position
    new_row, new_col = row, col

    if direction == "right":
        new_col = col + steps
    elif direction == "left":
        new_col = col - steps
    elif direction == "up":
        new_row = row - steps
    elif direction == "down":
        new_row = row + steps

    if 0 <= new_row < len(my_matrix) and 0 <= new_col < len(my_matrix[0]) and my_matrix[new_row][new_col] == ".":
        my_matrix[new_row][new_col] = "A"
        my_matrix[row][col] = "."

    return (new_row, new_col), my_matrix


def shoot_the_target(shooter_position, direction, my_matrix):

    row, col = shooter_position
    target_hit = []

    while True:
        if direction == "right":
            new_col = col + 1
            if new_col >= len(my_matrix[0]):
                break
            if my_matrix[row][new_col] == "x":
                target_hit.append([row, new_col])
                my_matrix[row][new_col] = "."
                break
            col = new_col
        elif direction == "left":
            new_col = col - 1
            if new_col < 0:
                break
            if my_matrix[row][new_col] == "x":
                target_hit.append([row, new_col])
                my_matrix[row][new_col] = "."
                break
            col = new_col
        elif direction == "up":
            new_row = row - 1
            if new_row < 0:
                break
            if my_matrix[new_row][col] == "x":
                target_hit.append([new_row, col])
                my_matrix[new_row][col] = "."
                break
            row = new_row
        elif direction == "down":
            new_row = row + 1
            if new_row >= len(my_matrix):
                break
            if my_matrix[new_row][col] == "x":
                target_hit.append([new_row, col])
                my_matrix[new_row][col] = "."
                break
            row = new_row

    return my_matrix, target_hit


command_count = int(input())
hit_targets = []

while command_count > 0:

    targets_left = are_targets_left(matrix)
    if targets_left == 0:
        break
    shooter = find_shooter(matrix)

    command = input().split()

    if command[0] == "move":
        direction, steps = command[1], int(command[2])

    elif command[0] == 'shoot':
        direction = command[1]
        matrix, target_hit = shoot_the_target(shooter, direction, matrix)
        if len(target_hit) > 0:
            hit_targets.append(target_hit)
    command_count -= 1

count_targets_left = are_targets_left(matrix)

if count_targets_left == 0:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {count_targets_left} targets left.")
for row in hit_targets:
    print(*row)
"""
# Dolu 2 testa ne minavat
"""
def simulate_shooting_range(field, commands):
    targets = []
    targets_hit = []
    position = None
    rows = len(field)
    cols = len(field[0])

    # Find the initial position and targets
    for row in range(rows):
        for col in range(cols):
            if field[row][col] == 'A':
                position = [row, col]
            elif field[row][col] == 'x':
                targets.append([row, col])

    def is_valid_position(row, col):
        return 0 <= row < rows and 0 <= col < cols

    def shoot_target(direction):
        row, col = position[0], position[1]
        if direction == 'up':
            while row >= 0:
                if [row, col] in targets:
                    targets_hit.append([row, col])
                    targets.remove([row, col])

                    break
                row -= 1
        elif direction == 'down':
            while row < rows:
                if [row, col] in targets:
                    targets_hit.append([row, col])
                    targets.remove([row, col])
                    break
                row += 1
        elif direction == 'left':
            while col >= 0:
                if [row, col] in targets:
                    targets_hit.append([row, col])
                    targets.remove([row, col])
                    break
                col -= 1
        elif direction == 'right':
            while col < cols:
                if [row, col] in targets:
                    targets_hit.append([row, col])
                    targets.remove([row, col])
                    break
                col += 1

    def move(direction, steps):
        row, col = position[0], position[1]
        if direction == 'up':
            row -= steps
        elif direction == 'down':
            row += steps
        elif direction == 'left':
            col -= steps
        elif direction == 'right':
            col += steps

        if is_valid_position(row, col) and field[row][col] == '.':
            position[0], position[1] = row, col

    for command in commands:
        if len(targets) == 0:
            break
        if command.startswith('shoot'):
            _, direction = command.split()
            shoot_target(direction)
        elif command.startswith('move'):
            _, direction, steps = command.split()
            move(direction, int(steps))
    if len(targets) == 0:
        print(f"Training completed! All {len(targets_hit)} targets hit.")
    else:
        print(f"Training not completed! {len(targets)} targets left.")
    [print(row) for row in targets_hit]



matrix = [[x for x in input().split()] for _ in range(5)]
N = int(input())
commands = []
for i in range(N):
    commands.append(input())

simulate_shooting_range(matrix, commands)
"""
"""
. . . . . 
. . . . . 
. A x . . 
. x . . . 
. x . . . 
2
shoot down
shoot right

. . . . . 
. . . . . 
. A . . . 
. . . . . 
. x . . . 
3
shoot down
move right 4
move left 1


"""