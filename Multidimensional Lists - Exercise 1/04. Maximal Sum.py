rows, cols = map(int, input().split())
matrix = [[int(x) for x in input().split()] for i in range(rows)]
temp_list = None
max_sum = float("-inf")

for row in range(rows - 2):
    for col in range(cols - 2):
        square_sum = (matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] +
                      matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] +
                      matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2])
        if max_sum < square_sum:
            max_sum = square_sum

            temp_list = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                         [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                         [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]]

print(f"Sum = {max_sum}")
for row in temp_list:
    print(' '.join(map(str, row)))

