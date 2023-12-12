rows, cols = map(int, input().split(", "))
matrix = [[int(el) for el in input().split()] for row in range(rows)]
result = []
for col in range(cols):
    sum_total = 0
    for row in range(rows):
        sum_total += matrix[row][col]
    print(sum_total)
