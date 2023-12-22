def find_opponents(room):
    opponents = 0
    for row in range(len(room)):
        for col in range(len(room[0])):
            if room[row][col] == 'P':
                opponents += 1
    return opponents


def find_me(room):
    for row in range(len(room)):
        for col in range(len(room[0])):
            if room[row][col] == 'B':
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


rows, cols = map(int, input().split())
room = [[el for el in input().split()]for _ in range(rows)]



curr_row, curr_col = find_me(room)
opponents_count = find_opponents(room)
opponents_touched = 0
moves_count = 0

while opponents_count != 0:
    command = input()
    if command == "Finish":
        break
    next_row, next_col = next_move(command, curr_row, curr_col)
    if next_row is None or next_col is None:
        continue
    cell = room[next_row][next_col]

    if cell == "O":
        continue
    if cell == "P":
        opponents_count -= 1
        opponents_touched += 1
    moves_count += 1
    room[curr_row][curr_col] = "-"
    room[next_row][next_col] = "B"

    curr_row, curr_col = next_row, next_col

print("Game over!")
print(f"Touched opponents: {opponents_touched} Moves made: {moves_count}")
