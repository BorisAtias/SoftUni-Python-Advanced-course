def stacked_queries(n):
    stack = []
    for i in range(n):

        command = input().split()

        if command[0] == "1":
            stack.append(int(command[1]))
        if len(stack) > 0:
            if command[0] == "2":
                stack.pop()
            elif command[0] == "3":
                print(max(stack))
            elif command[0] == "4":
                print(min(stack))

    return final_print(stack)

def final_print(stack):

    print(*stack[::-1], sep=", ")

n = int(input())

stacked_queries(n)

