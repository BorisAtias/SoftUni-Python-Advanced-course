numbers = list(map(int, input().split()))
target_number = int(input())

seen_numbers = {}

for number in numbers:
    difference = target_number - number
    if difference in seen_numbers:
        print(f"{difference} + {number} = {target_number}")

    seen_numbers[number] = True


# SoftUni using set()

numbers = list(map(int, input().split()))
target = int(input())

targets = set()
values_map = {}

for value in numbers:
    resulting_number = target - value
    targets.add(resulting_number)
    values_map[resulting_number] = value

for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f"{pair} + {value} = {target}")
    else:
        resulting_number = target - value
        targets.add(resulting_number)
        values_map[resulting_number] = value
