from collections import deque

choco_stack = [int(x) for x in input().split(",")]
milk_cups = deque(map(int, input().split(",")))

milk_shakes = 0

while milk_shakes < 5 and choco_stack and milk_cups:

    if milk_cups[0] <= 0 and choco_stack[-1] <= 0:
        milk_cups.popleft()
        choco_stack.pop()
        continue
    if milk_cups[0] <= 0:
        milk_cups.popleft()
        continue
    if choco_stack[-1] <= 0:
        choco_stack.pop()
        continue

    if milk_cups:
        if milk_cups[0] == choco_stack[-1]:
            milk_shakes += 1
            milk_cups.popleft()
            choco_stack.pop()
        else:
            milk_cups.rotate(-1)
            choco_stack[-1] -= 5

if milk_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(choco_stack) == 0:
    print("Chocolate: empty")
else:
    print(f"Chocolate: {', '.join(map(str, choco_stack))}")

if len(milk_cups) == 0:
    print("Milk: empty")
else:
    print(f"Milk: {', '.join(map(str, milk_cups))}")

