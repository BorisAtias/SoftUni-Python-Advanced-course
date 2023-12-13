rows, cols = map(int, input().split())
matrix = [[x for x in input().split()] for row in range(rows)]

c = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        curr_el = matrix[row][col]
        next_el = matrix[row][col + 1]
        below_curr_el = matrix[row + 1][col]
        below_next_el = matrix[row + 1][col + 1]

        if curr_el == next_el and curr_el == below_curr_el and curr_el == below_next_el:
            c += 1
print(c)