rows = int(input())

matrix = []

for i in range(rows):
    el = [int(x) for x in input().split(", ")]
    matrix.append(el)

even_matrix = []

for row_index in range(0, rows):
    even_matrix.append([])
    for col_index in range(len(matrix[row_index])):
        curr_el = matrix[row_index][col_index]
        if curr_el % 2 == 0:
            even_matrix[row_index].append(curr_el)

print(even_matrix)

#----------------------------------------------#

rows = int(input())

matrix = []

for i in range(rows):
    el = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(el)

print(matrix)


#-----------------------------------------#

matrix = [[int(el) for el in input().split(", ") if int(el) % 2 == 0] for row in range(int(input()))]

print(matrix)