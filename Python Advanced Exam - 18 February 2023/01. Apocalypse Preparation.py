from collections import deque

textiles = deque(map(int, input().split()))
medicaments_stack = list(map(int, input().split()))

production = {"Patch": 30, "Bandage": 40, "MedKit": 100}
production_count = { "MedKit": 0, "Bandage": 0, "Patch": 0}
while textiles and medicaments_stack:

    curr_textile = textiles.popleft()
    curr_medicament = medicaments_stack.pop()
    curr_result = curr_textile + curr_medicament
    for product, value in production.items():
        if curr_result == value:
            production_count[product] += 1
    if curr_result > 100:
        leftover = curr_result - 100
        production_count["MedKit"] += 1
        medicaments_stack[-1] += leftover
    if curr_result not in production.values() and curr_result < 100:
        curr_medicament += 10
        medicaments_stack.append(curr_medicament)

if not textiles and not medicaments_stack:
    print("Textiles and medicaments are both empty.")

else:
    if not textiles:
        print("Textiles are empty.")
    if not medicaments_stack:
        print("Medicaments are empty.")


sorted_count = sorted(production_count.items(), key=lambda x: (-x[1], x[0]))

for product, value in sorted_count:
    if value > 0:
        print(f"{product} - {value}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
if medicaments_stack:
    print(f"Medicaments left: {', '.join(map(str, (medicaments_stack[::-1])))}")
