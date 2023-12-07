water_quantity = int(input())

people = []

while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:

    command = input().split()

    if command[0] == "End":
        print(f"{water_quantity} liters left")
        break

    elif command[0].isnumeric():
        quantity = int(command[0])
        if quantity > water_quantity:
            print(f"{people[0]} must wait")
            people.remove(people[0])
        else:
            water_quantity -= int(command[0])
            print(f"{people[0]} got water")
            people.remove(people[0])
    elif command[0] == "refill":
        quantity = int(command[1])
        water_quantity += quantity


# Second way

from collections import deque

water_quantity = int(input())
people_queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    people_queue.append(command)

while True:
    command = input()
    if command == "End":
        break

    if command.startswith("refill"):
        _, refill_liters = command.split()
        refill_liters = int(refill_liters)
        water_quantity += refill_liters
    else:
        requested_liters = int(command)
        if requested_liters <= water_quantity:
            person_name = people_queue.popleft()
            water_quantity -= requested_liters
            print(f"{person_name} got water")
        else:
            person_name = people_queue.popleft()
            print(f"{person_name} must wait")

print(f"{water_quantity} liters left")

# Solution SoftUni
from collections import deque

quantity = int(input())
water_line = deque()
name = input()

while name != "Start":
    water_line.append(name)
    name = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) == 1:
        liters_to_give = int(data[0])
        persone_name = water_line.popleft()
        if liters_to_give <= quantity:
            print(f"{persone_name} got water")
            quantity -= liters_to_give
        else:
            print(f"{persone_name} must wait")
    else:
        liters_to_add = int(data[1])
        quantity += liters_to_add
    command = input()

print(f"{quantity} liters left")