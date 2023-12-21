rows, cols = map(int, input().split(","))
kitchen = [[el for el in input().split()[0]] for _ in range(rows)]


def is_there_cheese(kitchen):
    cheese_count = 0
    for i in range(len(kitchen)):
        for j in range(len(kitchen[0])):
            if kitchen[i][j] == 'C':
                cheese_count += 1
    return cheese_count

def find_mouse_position(kitchen):
    for row in range(len(kitchen)):
        for col in range(len(kitchen[0])):
            if kitchen[row][col] == 'M':
                return row, col


def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col):
    if command == 'up' and is_valid(current_row - 1, rows):
        return current_row - 1, current_col
    if command == 'down' and is_valid(current_row + 1, rows):
        return current_row + 1, current_col
    if command == 'left' and is_valid(current_col - 1, cols):
        return current_row, current_col - 1
    if command == 'right' and is_valid(current_col + 1, cols):
        return current_row, current_col + 1
    return None, None


cheese_count = is_there_cheese(kitchen)
curr_row, curr_col = find_mouse_position(kitchen)
kitchen[curr_row][curr_col] = "*"
while True:
    command = input()
    if command == "danger":
        print("Mouse will come back later!")
        kitchen[curr_row][curr_col] = "M"
        break
    next_row, next_col = next_move(command, curr_row, curr_col)
    if next_row is None or next_col is None:
        print("No more cheese for tonight!")
        kitchen[curr_row][curr_col] = "M"
        break
    cell = kitchen[next_row][next_col]
    if cell == "@":
        continue

    if cell == "T":
        print("Mouse is trapped!")
        kitchen[next_row][next_col] = "M"
        break
    if cell == "C":
        cheese_count -= 1
        kitchen[next_row][next_col] = "*"
    if cheese_count == 0:
        print("Happy mouse! All the cheese is eaten, good night!")
        kitchen[next_row][next_col] = "M"
        break
    curr_row, curr_col = next_row, next_col

for row in kitchen:
    print("".join(row))




