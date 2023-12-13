rows, cols = map(int, input().split())

matrix = [[chr(97 + row) + chr(97 + row + col) + chr(97 + row) for col in range(cols)] for row in range(rows)]

for row in matrix:
    print(" ".join(row))
