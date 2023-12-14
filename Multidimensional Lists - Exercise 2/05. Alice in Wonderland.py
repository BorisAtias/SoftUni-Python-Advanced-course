N = int(input())
matrix = [[x for x in input().split()] for _ in range(N)]


def find_alice(my_matrix, n):
    alice_position = None
    for row in range(n):
        for col in range(n):
            if my_matrix[row][col] == "A":
                alice_position = (row, col)
                return alice_position


def move_right(alice_position, my_matrix, tea_bags):
    row, col = alice_position
    new_col = col + 1

    if 0 <= new_col < len(my_matrix[0]):
        new_position = my_matrix[row][new_col]

        if new_position.isdigit():
            tea_bags += int(new_position)
        my_matrix[row][col] = "*"
        my_matrix[row][new_col] = "A"
        if new_position == "R":
            return None, my_matrix, tea_bags
        return alice_position, my_matrix, tea_bags

    return None, my_matrix, tea_bags


def move_left(alice_position, my_matrix, tea_bags):
    row, col = alice_position
    new_col = col - 1

    if 0 <= new_col < len(my_matrix[0]):
        new_position = my_matrix[row][new_col]
        if new_position.isdigit():
            tea_bags += int(new_position)
        my_matrix[row][col] = "*"
        my_matrix[row][new_col] = "A"
        if new_position == "R":
            return None, my_matrix, tea_bags
        return alice_position, my_matrix, tea_bags

    return None, my_matrix, tea_bags


def move_up(alice_position, my_matrix, tea_bags):
    row, col = alice_position
    new_row = row - 1

    if 0 <= new_row < len(my_matrix[0]):
        new_position = my_matrix[new_row][col]

        if new_position.isdigit():
            tea_bags += int(new_position)
        my_matrix[row][col] = "*"
        my_matrix[new_row][col] = "A"
        if new_position == "R":
            return None, my_matrix, tea_bags
        return alice_position, my_matrix, tea_bags
    return None, my_matrix, tea_bags


def move_down(alice_position, my_matrix, tea_bags):
    row, col = alice_position
    new_row = row + 1

    if 0 <= new_row < len(my_matrix[0]):
        new_position = my_matrix[new_row][col]

        if new_position.isdigit():
            tea_bags += int(new_position)
        my_matrix[row][col] = "*"
        my_matrix[new_row][col] = "A"
        if new_position == "R":
            return None, my_matrix, tea_bags
        return alice_position, my_matrix, tea_bags

    return None, my_matrix, tea_bags


total_tea_bags = 0
is_out = False

while total_tea_bags < 10 and not is_out:
    alice = find_alice(matrix, N)
    command = input()

    if command == "right":
        alice, matrix, total_tea_bags = move_right(alice, matrix, total_tea_bags)
    elif command == "left":
        alice, matrix, total_tea_bags = move_left(alice, matrix, total_tea_bags)
    elif command == "up":
        alice, matrix, total_tea_bags = move_up(alice, matrix, total_tea_bags)
    elif command == "down":
        alice, matrix, total_tea_bags = move_down(alice, matrix, total_tea_bags)

    if alice is None:
        is_out = True
        break

alice = find_alice(matrix, N)
row, col = alice
matrix[row][col] = "*"

if total_tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*row) for row in matrix]