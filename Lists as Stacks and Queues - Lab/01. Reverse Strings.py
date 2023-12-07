def reverse_string(string):
    rev_str = string[::-1]
    print(rev_str)

text = input()

reverse_string(text)

# Using Stack

text = list(input())
stack = []

for i in range(len(text)):
    stack.append(text.pop())

print("".join(stack))

# or ....

text = list(input())

while text:
    print(text.pop(), end="")
