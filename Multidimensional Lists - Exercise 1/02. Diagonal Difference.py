matrix = [[int(x) for x in input().split()] for i in range(int(input()))]

primary_diagonal = [matrix[row][row] for row in range(len(matrix))]
secondary_diagonal = [matrix[row][len(matrix) - row - 1] for row in range(len(matrix))]

diff = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(abs(diff))




