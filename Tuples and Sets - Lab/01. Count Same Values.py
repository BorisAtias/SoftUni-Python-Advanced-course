values = input().split()

counted_values = []

for i in values:
    if not i in counted_values:
        print(f"{float(i)} - {values.count(i)} times")

    counted_values.append(i)


# Second way


values = input().split()


number_counts = {}

for num in values:
    num = float(num)
    if num in number_counts:
        number_counts[num] += 1
    else:
        number_counts[num] = 1

for num, count in number_counts.items():
    print(f"{num:.1f} - {count} times")


# SoftUni way

values = tuple(float(el) for el in input().split())

number_counts = {}

for num in values:
    if num not in number_counts:
        number_counts[num] = values.count(num)
        print(f"{num:.1f} - {values.count(num)} times")