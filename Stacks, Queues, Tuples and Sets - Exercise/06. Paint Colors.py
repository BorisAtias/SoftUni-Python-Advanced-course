from collections import deque

main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": {"red", "yellow"}, "purple": {"red", "blue"}, "green": {"yellow", "blue"}}
sub_strings = deque(input().split())

colors_found = []

while sub_strings:

    first_el = sub_strings.popleft()
    second_el = sub_strings.pop() if sub_strings else ""

    for color in (first_el + second_el, second_el + first_el):
        if color in main_colors or color in secondary_colors:
            colors_found.append(color)
            break
    else:
        for char in (first_el[0:-1], second_el[0:-1]):
            if char:
                sub_strings.insert(len(sub_strings) // 2, char)


for color in set(secondary_colors.keys()).intersection(colors_found):
    if not secondary_colors[color].issubset(colors_found):
        colors_found.remove(color)

print(colors_found)