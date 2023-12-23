from collections import deque

initial_fuel_stack = deque([int(x) for x in input().split()])
additional_consumption_index = deque([int(x) for x in input().split()])
amount_of_fuel_needed = deque([int(x) for x in input().split()])
counter = 0
altitudes_reached = []

while initial_fuel_stack and additional_consumption_index and amount_of_fuel_needed:
    curr_initial_fuel = initial_fuel_stack.pop()
    curr_additional_consumption = additional_consumption_index.popleft()
    curr_result = curr_initial_fuel - curr_additional_consumption
    if curr_result < amount_of_fuel_needed[0]:
        print(f"John did not reach: Altitude {counter + 1}")
        break

    else:
        counter += 1
        print(f"John has reached: Altitude {counter}")
        altitudes_reached.append(f"Altitude {counter}")
        amount_of_fuel_needed.popleft()


if amount_of_fuel_needed and counter > 0:
    print(f"John failed to reach the top.\nReached altitudes: {', '.join(altitudes_reached)}")
elif counter == 0:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")