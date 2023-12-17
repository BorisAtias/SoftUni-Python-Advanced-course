intersections_count = int(input())

intersections = []
longest_range = []
for i in range(intersections_count):
    available_ranges = input().split("-")
    first_range = available_ranges[0].split(",")
    second_range = available_ranges[1].split(",")
    start_1, end_1 = int(first_range[0]), int(first_range[1])
    start_2, end_2 = int(second_range[0]), int(second_range[1])
    intersections.append(start_1)
    intersections.append(end_1)
    intersections.append(start_2)
    intersections.append(end_2)
    intersections.sort()
    intersections.pop(0)
    intersections.pop(-1)
    go = intersections.copy()
    longest_range.append(go)
    del intersections[0::]

index_position = 0
curr_max = 0
for i in longest_range:
    res = i[1] - i[0]
    if res > curr_max:
        curr_max = res
        index_position = longest_range.index(i)

result = []

start, end = longest_range[index_position][0], longest_range[index_position][1]

for i in range(start, end + 1):
    result.append(i)

print(f"Longest intersection is {result} with length {len(result)}")

# Using Sets

N = int(input())

longest_intersection = set()
max_intersection_length = 0

for _ in range(N):
    ranges = input().split("-")
    first_range = list(map(int, ranges[0].split(",")))
    second_range = list(map(int, ranges[1].split(",")))

    intersection = set(range(first_range[0], first_range[1] + 1)).intersection(set(range(second_range[0], second_range[1] + 1)))
    intersection_length = len(intersection)

    if intersection_length > max_intersection_length:
        max_intersection_length = intersection_length
        longest_intersection = intersection

sorted_longest_intersection = sorted(list(longest_intersection))

print(f"Longest intersection is [{', '.join(map(str, sorted_longest_intersection))}] with length {max_intersection_length}")
