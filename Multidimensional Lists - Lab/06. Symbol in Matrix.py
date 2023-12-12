rows = int(input())

matrix = []

for row in range(rows):
    el = list(input())
    matrix.append(el)

searched_element = input()
position = None
for row in range(rows):
    if position:
        break
    for col in range(len(matrix[row])):
        curr_el = matrix[row][col]
        if curr_el == searched_element:
            position = ((row, col))
            print(position)
            break

if not position:
    print(f"{searched_element} does not occur in the matrix")

