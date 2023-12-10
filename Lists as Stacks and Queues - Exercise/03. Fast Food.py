from collections import deque

food_quantity = int(input())
orders_queue = deque()
orders = input().split()

for order in orders:
    orders_queue.append(int(order))

biggest_order = max(orders_queue)

while orders_queue:
    curr_order = orders_queue[0]
    if curr_order <= food_quantity:
        food_quantity -= curr_order
        orders_queue.popleft()
    else:
        break

print(biggest_order)

if not orders_queue:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, orders_queue))}")

