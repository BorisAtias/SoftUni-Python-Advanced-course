matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]
sum_total = 0
for row in range(len(matrix)):
    sum_total += matrix[row][row]

print(sum_total)