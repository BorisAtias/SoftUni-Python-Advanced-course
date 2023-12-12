data = input().split(", ")
rows = int(data[0])
cols = int(data[1])

matrix = []
sum_total = 0
for _ in range(rows):
    el = [int(x) for x in input().split(", ")]
    sum_total += sum(el)
    matrix.append(el)

print(sum_total)
print(matrix)