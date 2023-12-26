from collections import deque


def find_squirrel_position(forest):
    for row in range(len(forest)):
        for col in range(len(forest[0])):
            if forest[row][col] == 's':
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


rows = int(input())
commands_list = deque(map(str, input().split(", ")))
forest = [[el for el in input().split()[0]] for _ in range(rows)]
cols = rows
hazelnuts_count = 0
curr_row, curr_col = find_squirrel_position(forest)
forest[curr_row][curr_col] = "*"
are_more_hazelnuts = True
while commands_list:
    command = commands_list.popleft()
    next_row, next_col = next_move(command, curr_row, curr_col)
    if next_row is None or next_col is None:
        print(f"The squirrel is out of the field.\nHazelnuts collected: {hazelnuts_count}")
        are_more_hazelnuts = False
        break
    cell = forest[next_row][next_col]

    if cell == "t":
        print(f"Unfortunately, the squirrel stepped on a trap...\nHazelnuts collected: {hazelnuts_count}")
        are_more_hazelnuts = False
        break
    if cell == "h":
        hazelnuts_count += 1
        forest[next_row][next_col] = "*"
        if hazelnuts_count == 3:
            print(f"Good job! You have collected all hazelnuts!\nHazelnuts collected: {hazelnuts_count}")
            are_more_hazelnuts = False
            break
    curr_row, curr_col = next_row, next_col


if are_more_hazelnuts and hazelnuts_count < 3:
    print(f"There are more hazelnuts to collect.\nHazelnuts collected: {hazelnuts_count}")


#----------Second variant-------------------------------------------#


from collections import deque

# checks the validity of indexes
def is_valid_idx(row, col) -> bool:
    return 0 <= row < size and 0 <= col < size


size = int(input())
commands = deque(input().split(", "))
# Define possible moves
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),}
hazelnuts = 0
field = []
squirrel_row, squirrel_col = 0, 0

# Read the field and find the squirrel's initial position
for r in range(size):
    rows = list(input())
    field.append(rows)
    if "s" in rows:
        squirrel_row = r
        squirrel_col = rows.index("s")

while commands:
    direction = commands.popleft()
    field[squirrel_row][squirrel_col] = "*"  # Mark the previous position
    # Calculate the new position based on the selected direction
    new_row = squirrel_row + moves[direction][0]
    new_col = squirrel_col + moves[direction][1]
    squirrel_row, squirrel_col = new_row, new_col

    if not is_valid_idx(new_row, new_col):
        print("The squirrel is out of the field.")
        break
    if field[squirrel_row][squirrel_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    if field[squirrel_row][squirrel_col] == "h":
        hazelnuts += 1
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break

else:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")