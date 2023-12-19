import math
from collections import deque

expression = deque(x for x in input().split())

holder = []
sum_total = 0
c = 0
operators = ["*", "/", "-", "+"]

while c != len(expression):
    for i in expression:
        c += 1
        if i not in operators:
            holder.append(int(i))
        else:
            if i == "*":
                sum_total = holder[0]
                holder.pop(0)
                for num in holder:
                    sum_total = sum_total * num
            elif i == '/':
                sum_total = holder[0]
                holder.pop(0)
                for num in holder:
                    sum_total = math.floor(sum_total / num)
            elif i == "+":
                sum_total = sum(holder)
            elif i == "-":
                sum_total = holder[0]
                holder.pop(0)
                for num in holder:
                    sum_total = sum_total - num

            del holder[::]
            holder.append(sum_total)
            sum_total = 0

sum_total = holder[0]
print(sum_total)


