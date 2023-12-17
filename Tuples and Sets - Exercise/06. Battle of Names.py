from math import floor

N = int(input())

even = set()
odd = set()

for i in range(1, N + 1):
    name = input()
    total_sum = 0
    for char in name:
        total_sum += ord(char)

    res = floor(total_sum / i)
    if res % 2 == 0:
        even.add(res)
    else:
        odd.add(res)

even_values = list(even)
odd_values = list(odd)

if sum(even_values) == sum(odd_values):
    union_values = even.union(odd)
    print(", ".join(map(str, union_values)))
elif sum(odd_values) > sum(even_values):
    different_values = odd.difference(even)
    print(", ".join(map(str, different_values)))
else:
    symmetric_difference_values = even.symmetric_difference(odd)
    print(", ".join(map(str, symmetric_difference_values)))

