"""from collections import deque
rows, cols = map(int, input().split())
snake = deque(input())

# Initialize variables for current position and direction
row, col, direction = 0, 0, 1  # Direction: 1 (right), -1 (left)

# Initialize an empty matrix
matrix = [['' for _ in range(cols)] for _ in range(rows)]

for row in range(rows):
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = snake[0]
        else:
            matrix[row][-1 - col] = snake[0]
        snake.rotate(-1)

[print(*row, sep="") for row in matrix]
"""


def snake_moves():
  # Get the dimensions of the field
  n, m = map(int, input().split())

  # Get the snake string
  snake = input()

  # Create an empty field
  field = [['' for _ in range(m)] for _ in range(n)]

  # Initialize the snake index
  snake_index = 0

  # Traverse the field
  for row in range(n):
    if row % 2 == 0:  # Move from left to right
      for col in range(m):
        field[row][col] = snake[snake_index]
        snake_index = (snake_index + 1) % len(snake)  # Cycle through the snake string
    else:  # Move from right to left
      for col in range(m - 1, -1, -1):
        field[row][col] = snake[snake_index]
        snake_index = (snake_index + 1) % len(snake)  # Cycle through the snake string

  # Print the snake path
  for row in field:
    print(''.join(row))


snake_moves()