rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]


def is_valid(row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def add(my_matrix, row, col, value):
    if is_valid(row, col):
        my_matrix[row][col] += value
    else:
        print("Invalid coordinates")

    return my_matrix


def subtract(my_matrix, row, col, value):
    if is_valid(row, col):
        my_matrix[row][col] -= value
    else:
        print("Invalid coordinates")

    return my_matrix


while True:

    command = input().split()
    if command[0] == "END":
        for row in matrix:
            print(" ".join(map(str, row)))
        break
    if command[0] == "Add":
        index_row, index_col, value = int(command[1]), int(command[2]), int(command[3])
        matrix = add(matrix, index_row, index_col, value)
    elif command[0] == "Subtract":
        index_row, index_col, value = int(command[1]), int(command[2]), int(command[3])
        matrix = subtract(matrix, index_row, index_col, value)

