def add_first(sequence_1, numbers):
    num = set(numbers)
    sequence_1.update(num)
    return sequence_1

def add_second(sequence_2, numbers):
    num = set(numbers)
    sequence_2.update(num)
    return sequence_2

def remove_first(sequence_1, numbers):
    to_remove = set(numbers)
    sequence_1.difference_update(to_remove)
    return sequence_1

def remove_second(sequence_2, numbers):
    to_remove = set(numbers)
    sequence_2.difference_update(to_remove)
    return sequence_2

def is_subset(sequence_1, sequence_2):
    return set(sequence_1).issubset(set(sequence_2)) or set(sequence_2).issubset(set(sequence_1))


first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))

count = int(input())

for i in range(count):
    command = input().split()

    if command[0] == 'Add':
        nums = list(map(int, command[2::]))
        if command[1] == "First":
            first_sequence = add_first(first_sequence, nums)
        else:
            second_sequence = add_second(second_sequence, nums)
    elif command[0] == "Remove":
        nums = list(map(int, command[2::]))
        if command[1] == "First":
            first_sequence = remove_first(first_sequence, nums)
        else:
            second_sequence = remove_second(second_sequence, nums)
    elif command[0] == "Check":
        result = is_subset(first_sequence, second_sequence)
        print(result)

first_sequence = sorted(first_sequence)
second_sequence = sorted(second_sequence)

print(", ".join(map(str, first_sequence)))
print(", ".join(map(str, second_sequence)))
