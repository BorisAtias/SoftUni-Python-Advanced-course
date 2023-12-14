N = int(input())
matrix = [[x for x in input().split()] for _ in range(N)]

def find_b(my_matrix, n):
    B_position = None
    for row in range(n):
        for col in range(n):
            if my_matrix[row][col] == "B":
                B_position = (row, col)
                return B_position

def move_right(B_position, my_matrix):
    row, col = B_position
    eggs = 0
    path = []
    while col < len(my_matrix[0]) and my_matrix[row][col] != "X":
        if my_matrix[row][col] == "B":
            col += 1
            continue
        else:
            eggs += int(my_matrix[row][col])
            path.append([row,col])
            col += 1

    return eggs, path

def move_left(B_position, my_matrix):
    row, col = B_position
    eggs = 0
    path = []
    while col >= 0 and my_matrix[row][col] != "X":
        if my_matrix[row][col] == "B":
            col -= 1
            continue
        else:
            eggs += int(my_matrix[row][col])
            path.append([row, col])
            col -= 1

    return eggs, path

def move_up(B_position, my_matrix):
    row, col = B_position
    eggs = 0
    path = []
    while row >= 0 and my_matrix[row][col] != "X":
        if my_matrix[row][col] == "B":
            row -= 1
            continue
        else:
            eggs += int(my_matrix[row][col])
            path.append([row, col])
            row -= 1

    return eggs, path


def move_down(B_position, my_matrix):
    row, col = B_position
    eggs = 0
    path = []
    while row < len(my_matrix) and my_matrix[row][col] != "X":
        if my_matrix[row][col] == "B":
            row += 1
            continue
        else:
            eggs += int(my_matrix[row][col])
            path.append([row, col])
            row += 1

    return eggs, path

max_eggs = float("-inf")
best_direction = ""
path_taken = []
bunny_position = find_b(matrix, N)


eggs_right, path_right = move_right(bunny_position, matrix)
if eggs_right > max_eggs:
    max_eggs = eggs_right
    best_direction = "right"
    path_taken = path_right

eggs_left, path_left = move_left(bunny_position, matrix)
if eggs_left > max_eggs:
    max_eggs = eggs_left
    best_direction = "left"
    path_taken = path_left

eggs_up, path_up = move_up(bunny_position, matrix)
if eggs_up > max_eggs:
    max_eggs = eggs_up
    best_direction = "up"
    path_taken = path_up

eggs_down, path_down = move_down(bunny_position, matrix)
if eggs_down > max_eggs:
    max_eggs = eggs_down
    best_direction = "down"
    path_taken = path_down

print(best_direction)
for path in path_taken:
    print(path)
print(max_eggs)


# SoftUni down

n = int(input())
matrix = []
bunny = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "B":
            bunny = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
max_eggs = float("-inf")
max_direction = ""
max_eggs_matrix = []

for direction, move in possible_moves.items():
    eggs = 0
    current_eggs_matrix = []
    row = bunny[0] + move[0]
    col = bunny[1] + move[1]

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "X":
            break
        eggs += int(matrix[row][col])
        current_eggs_matrix.append([row, col])
        row += move[0]
        col += move[1]

    if eggs > max_eggs and current_eggs_matrix:
        max_eggs = eggs
        max_direction = direction
        max_eggs_matrix = current_eggs_matrix

print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)

