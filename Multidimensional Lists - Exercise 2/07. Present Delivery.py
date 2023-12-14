presents_count = int(input())
matrix = [[el for el in input().split()] for _ in range(int(input()))]
print(matrix)


def find_santa(my_matrix):
    santa = None
    for row in range(len(my_matrix)):
        for col in range(len(my_matrix)):
            if my_matrix[row][col] == "S":
                santa = (row,col)
                return santa


def move_right(santa, my_matrix, presents):
    row, col = santa
    new_col = col + 1
    santa = "-"
    if 0 <= new_col < len(matrix[0]):
        new_position = my_matrix[row][new_col]
        santa = new_position
        new_position = "S"
        if new_position == "C":
            cookies(santa, my_matrix, presents, directions)
        elif new_position == "V":
            presents -= 1
    return santa, my_matrix, presents


def move_left(santa, my_matrix, presents):
    row, col = santa
    new_col = col - 1
    santa = "-"
    if 0 <= new_col < len(matrix[0]):
        new_position = my_matrix[row][new_col]
        santa = new_position
        new_position = "S"
        if new_position == "C":
            cookies(santa, my_matrix, presents, directions)
        elif new_position == "V":
            presents -= 1
    return santa, my_matrix, presents


def move_up(santa, my_matrix, presents):
    row, col = santa
    new_row = row - 1
    santa = "-"
    if 0 <= new_row < len(matrix[0]):
        new_position = my_matrix[row][new_row]
        santa = new_position
        new_position = "S"
        if new_position == "C":
            cookies(santa, my_matrix, presents, directions)
        elif new_position == "V":
            presents -= 1
    return santa, my_matrix, presents


def move_down(santa, my_matrix, presents):
    row, col = santa
    new_row = row + 1
    santa = "-"
    if 0 <= new_row < len(matrix[0]):
        new_position = my_matrix[row][new_row]
        santa = new_position
        new_position = "S"
        if new_position == "C":
            cookies(santa, my_matrix, presents, directions)
        elif new_position == "V":
            presents -= 1
    return santa, my_matrix, presents


def cookies(santa, my_matrix, presents, directions):
    if my_matrix["up"] == "V" or my_matrix["up"] == "X":
        presents -= 1
    if my_matrix["down"] == "V" or my_matrix["down"] == "X":
        presents -= 1
    if my_matrix["left"] == "V" or my_matrix["left"] == "X":
        presents -= 1
    if my_matrix["right"] == "V" or my_matrix["right"] == "X":
        presents -= 1

    return presents

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0, -1]
}

#while True:
#    pass

# Dolu 2 testa ne izlizat
"""
def distribute_presents(matrix, presents, count_V, row, col):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            if matrix[new_row][new_col] == 'V' or matrix[new_row][new_col] == 'X':
                if matrix[new_row][new_col] == 'V':
                    count_V += 1
                matrix[new_row][new_col] = '-'
                presents -= 1

    return matrix, presents, count_V

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

def check_nice_kids(matrix):
    count_nice_kids = sum(row.count('V') for row in matrix)
    return count_nice_kids

m = int(input())  # Number of presents
n = int(input())  # Size of the neighborhood

# Read the matrix
matrix = [[el for el in input().split()] for _ in range(n)]

# Initialize variables
nice_kids = check_nice_kids(matrix)
santa_row = None
santa_col = None
presents = m
ran_out_of_presents = False
count_V = 0

# Find Santa's position
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'S':
            santa_row = i
            santa_col = j
            break

# Process commands
while True:
    command = input()
    if command == 'Christmas morning' or presents == 0:
        break

    matrix[santa_row][santa_col] = '-'

    if command == 'up':
        santa_row -= 1
    elif command == 'down':
        santa_row += 1
    elif command == 'left':
        santa_col -= 1
    elif command == 'right':
        santa_col += 1

    if 0 <= santa_row < n and 0 <= santa_col < n:
        cell = matrix[santa_row][santa_col]
        if cell == 'V':
            count_V += 1
            presents -= 1
            matrix[santa_row][santa_col] = '-'
        elif cell == 'X':
            matrix[santa_row][santa_col] = '-'
        elif cell == 'C':
            matrix[santa_row][santa_col] = '-'
            matrix, presents, count_V = distribute_presents(matrix, presents, count_V, santa_row, santa_col)
    matrix[santa_row][santa_col] = 'S'  # Update Santa's position


    if presents == 0:
        ran_out_of_presents = True
        print("Santa ran out of presents!")
        break


print_matrix(matrix)


if (nice_kids - count_V) > 0:
    print(f"No presents for {nice_kids - count_V} nice kid/s.")
else:
    print(f"Good job, Santa! {count_V} happy nice kid/s.")
"""