from collections import deque

time_to_complete_task = deque(map(int, input().split()))
tasks_stack = list(map(int, input().split()))

duck_types = {"Darth Vader Ducky": range(0, 61), "Thor Ducky": range(61, 121),
              "Big Blue Rubber Ducky": range(121, 181), "Small Yellow Rubber Ducky": range(181, 241)}

production_count = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

while time_to_complete_task and tasks_stack:

    curr_time_for_task = time_to_complete_task.popleft()
    curr_task = tasks_stack.pop()
    curr_result = curr_time_for_task * curr_task

    if curr_result > 240:
        curr_task -= 2
        tasks_stack.append(curr_task)
        time_to_complete_task.append(curr_time_for_task)
        continue
    for duck, value in duck_types.items():
        if curr_result in value:
            production_count[duck] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for duck, count in production_count.items():
    print(f"{duck}: {count}")


