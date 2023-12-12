rows, cols = map(int, input().split(", "))
matrix = [[int(el) for el in input().split(", ")] for row in range(rows)]

max_sum = float("-inf")
max_sum_sub_matrix = []
for row in range(rows - 1):
    for col in range(cols - 1):
        curr_el = matrix[row][col]
        next_el = matrix[row][col + 1]
        below_el = matrix[row +1][col]
        second_below = matrix[row + 1][col + 1]
        sum_el = curr_el + next_el + below_el + second_below

        if max_sum < sum_el:
            max_sum = sum_el
            max_sum_sub_matrix = [[curr_el, next_el], [below_el, second_below]]

print(*max_sum_sub_matrix[0])
print(*max_sum_sub_matrix[1])
print(max_sum)