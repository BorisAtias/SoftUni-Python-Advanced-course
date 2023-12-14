N = int(input())
matrix = [list(input()) for _ in range(N)]

def is_inside_board(x, y, n):
    return 0 <= x < n and 0 <= y < n


def calculate_attacks(x, y, N, board):
    moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    num_attacks = 0

    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if is_inside_board(new_x, new_y, N) and board[new_x][new_y] == 'K':
            num_attacks += 1

    return num_attacks

total_removed = 0

while True:
    max_attacks = 0
    knight_to_remove = None

    for row in range(N):
        for col in range(N):
            if matrix[row][col] == "K":
                num_attacks = calculate_attacks(row, col, N, matrix)
                if num_attacks > max_attacks:
                    max_attacks = num_attacks
                    knight_to_remove = (row, col)

    if knight_to_remove is not None:
        matrix[knight_to_remove[0]][knight_to_remove[1]] = "0"
        total_removed += 1
    else:
        break

print(total_removed)
