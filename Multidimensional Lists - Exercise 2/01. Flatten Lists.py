all_lists = input().split("|")
matrix = []

for sub_list in all_lists[::-1]:
    curr_el = sub_list.split()
    for el in curr_el:
        matrix.append(el)

print(" ".join(map(str, matrix)))
