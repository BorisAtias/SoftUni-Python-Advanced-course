from collections import deque

tools = deque(map(int, input().split()))
substances_stack = list(map(int, input().split()))
challenges = list(map(int, input().split()))

while tools and substances_stack and challenges:
    curr_tool = tools.popleft()
    curr_substance = substances_stack.pop()
    curr_res = curr_tool * curr_substance

    if curr_res in challenges:
        challenges.remove(curr_res)
    else:
        tools.append(curr_tool + 1)
        if curr_substance - 1 <= 0:
            continue
        else:
            substances_stack.append(curr_substance - 1)

if not substances_stack and challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
if tools:
    print(f"Tools: {', '.join(map(str, tools))}")
if substances_stack:
    print(f"Substances: {', '.join(map(str, substances_stack))}")
if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")
