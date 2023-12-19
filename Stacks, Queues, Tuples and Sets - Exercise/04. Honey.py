from collections import deque

bees = deque(map(int, input().split()))
nectar_stack = list(int(x) for x in input().split())
symbols_sequence = deque(map(str, input().split()))

honey_produced = 0

while len(bees) != 0 and len(nectar_stack) != 0:

    if bees[0] <= nectar_stack[-1]:
        if nectar_stack[-1] == 0 and symbols_sequence[0] == "/":
            bees.popleft()
            symbols_sequence.popleft()
            nectar_stack.pop()
            continue
        else:
            if symbols_sequence[0] == "*":
                honey_produced += (bees[0] * nectar_stack[-1])
            elif symbols_sequence[0] == "-":
                honey_produced += abs(bees[0] - nectar_stack[-1])
            elif symbols_sequence[0] == "+":
                honey_produced += (bees[0] + nectar_stack[-1])
            elif symbols_sequence[0] == "/":
                honey_produced += abs(bees[0] / nectar_stack[-1])

            bees.popleft()
            symbols_sequence.popleft()
            nectar_stack.pop()
    else:
        nectar_stack.pop()

print(f"Total honey made: {honey_produced}")

if len(bees) > 0:
    print(f"Bees left: {', '.join(map(str, bees))}")
if len(nectar_stack) > 0:
    print(f"Nectar left: {', '.join(map(str, nectar_stack))}")
