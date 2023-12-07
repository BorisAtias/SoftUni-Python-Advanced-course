kids = input().split()
toss_count = int(input())
c = 0

while len(kids) != 1:

    for kid in range(len(kids)):
        c += 1
        if toss_count == 1:
            kid = 0
            if len(kids) == 1:
                break
        if c == toss_count:
            print(f"Removed {kids[kid]}")
            kids.remove(kids[kid])
            c = 0

print(f"Last is {kids[0]}")



# SoftUni solution

from collections import deque

children = deque(input().split())

n = int(input()) - 1

while len(children) != 1:
    children.rotate(-n)
    print(f"{children.popleft()}")


print(f"Last is {children.popleft()}")