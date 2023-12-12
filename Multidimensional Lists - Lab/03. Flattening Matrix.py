matrix = [[int(el) for el in input().split(", ")] for row_index in range(int(input()))]


flattened = [num for sub_list in matrix for num in sub_list]
print(flattened)


#------------------------------------------#

rows = int(input())
matrix = [map(int, input().split(", ")) for _ in range(rows)]

flattened = [num for sub_list in matrix for num in sub_list]
print(flattened)