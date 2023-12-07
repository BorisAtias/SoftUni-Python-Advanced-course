costumers = []

while True:

    command = input()

    if command == "End":
        print(f"{len(costumers)} people remaining.")
        break

    elif command == "Paid":
        print(*costumers, sep="\n")
        del costumers[0:]
    else:
        costumers.append(command)

# Whith qeue

from collections import deque

customer_list = deque()
name = input()

while name != "End":

    if name == " Paid":
        while customer_list:
            print(customer_list.popleft())
    else:
        customer_list.append(name)
    name = input()

print(f"{len(costumers)} people remaining.")
