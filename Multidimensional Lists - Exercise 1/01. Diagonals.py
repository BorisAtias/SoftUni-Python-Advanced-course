matrix = [[int(x) for x in input().split(", ")] for i in range(int(input()))]

primary_diagonal = [matrix[row][row] for row in range(len(matrix))]
secondary_diagonal = [matrix[row][len(matrix) - row - 1] for row in range(len(matrix))]

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")