rows, cols = map(int, input().split())

matrix = [[x for x in input().split()] for i in range(rows)]


def is_index_valid(i, j, matrix_rows, matrix_cols):
    return 0 <= i < matrix_rows and 0 <= j < matrix_cols


def swap(my_matrix, index1, index2, index3, index4):
    if is_index_valid(index1, index2, rows, cols) and is_index_valid(index3, index4, rows, cols):
        my_matrix[index1][index2], my_matrix[index3][index4] = my_matrix[index3][index4], my_matrix[index1][index2]
        print_result(my_matrix)
    else:
        print("Invalid input!")

    return my_matrix


def print_result(my_matrix):
    for row in my_matrix:
        print(' '.join(map(str, row)))


while True:

    command = input().split()
    if command[0] == "END":
        break

    if command[0] == "swap":
        if len(command) == 5:
            first_el, second_el, third_el, fourth_el = int(command[1]), int(command[2]), int(command[3]), int(command[4])
            matrix = swap(matrix, first_el, second_el, third_el, fourth_el)
        else:
            print("Invalid input!")

    else:
        print("Invalid input!")
