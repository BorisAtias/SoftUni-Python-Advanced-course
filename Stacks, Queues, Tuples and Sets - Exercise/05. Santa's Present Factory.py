from collections import deque

materials_stack = list(int(x) for x in input().split())
magic_values = deque(map(int, input().split()))

toys = []
energy_levels = [150, 250, 300, 400]

while len(materials_stack) > 0 and len(magic_values) > 0:

    if materials_stack[-1] == 0 or magic_values[0] == 0:
        if materials_stack[-1] == 0:
            materials_stack.pop()
        if magic_values[0] == 0:
            magic_values.popleft()
        continue

    curr_magic_value = magic_values.popleft()
    curr_material = materials_stack.pop()
    energy_result = curr_material * curr_magic_value

    if energy_result == 150:
        toys.append("Doll")
    elif energy_result == 250:
        toys.append("Train")
    elif energy_result == 300:
        toys.append("Teddy bear")
    elif energy_result == 400:
        toys.append("Bicycle")
    else:
        if energy_result < 0:
            materials_stack.append(curr_material + curr_magic_value)
        else:
            materials_stack.append(curr_material + 15)


if "Doll" in toys and "Train" in toys or "Teddy bear" in toys and "Bicycle" in toys:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if len(materials_stack) > 0:
    print(f"Materials left: {', '.join(map(str, materials_stack[::-1]))}")
if len(magic_values) > 0:
    print(f"Magic left: {', '.join(map(str, magic_values))}")
sorted_toys = sorted(set(toys))

for toy in sorted_toys:
    print(f"{toy}: {toys.count(toy)}")



"""from collections import deque

materials = deque([int(x) for x in input().split()])
magic_values = deque([int(x) for x in input().split()])

magic_needed = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
                }
presents_dict = {}

is_done = False

while len(materials) > 0 and len(magic_values) > 0:
    if materials[-1] == 0 or magic_values[0] == 0:
        if materials[-1] == 0:
            material = materials.pop()

        if magic_values[0] == 0:
            magic_level = magic_values.popleft()

        continue

    material = materials.pop()
    magic_level = magic_values.popleft()

    current_magic_level = material * magic_level

    if current_magic_level in magic_needed.keys():
        if magic_needed[current_magic_level] in presents_dict:
            presents_dict[magic_needed[current_magic_level]] += 1
        else:
            presents_dict[magic_needed[current_magic_level]] = 1

        if "Doll" in presents_dict.keys() and "Train" in presents_dict.keys():
            is_done = True
        if "Teddy bear" in presents_dict.keys() and "Bicycle" in presents_dict.keys():
            is_done = True
    else:
        if current_magic_level <= 0:
            material_to_add = material + magic_level
            materials.append(material_to_add)
        else:
            material += 15
            materials.append(material)

if is_done:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials][::-1])}')

if magic_values:
    print(f'Magic left: {", ".join([str(x) for x in magic_values])}')

sorted_presents = list(presents_dict.keys())
sorted_presents.sort()

for present in sorted_presents:
    print(f"{present}: {presents_dict[present]}")"""