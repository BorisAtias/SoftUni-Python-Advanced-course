def reverse_string_with_stack(input_string):

    integers = [int(x) for x in input_string.split()]

    stack = []

    for num in integers:
        stack.append(num)

    reversed_integers = []
    while stack:
        reversed_integers.append(stack.pop())

    reversed_string = ' '.join(map(str, reversed_integers))

    return reversed_string

input_string = input()

reversed_result = reverse_string_with_stack(input_string)

print(reversed_result)
