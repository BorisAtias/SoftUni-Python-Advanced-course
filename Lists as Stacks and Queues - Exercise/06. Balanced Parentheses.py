expression = input()
stack = []
count = 0
for i in expression:
    if i in ['(', '[', '{']:
        stack.append(i)
    else:
        if not stack:
            count += 1
            break
        curr_char = stack.pop()
        if curr_char == "{":
            if i != '}':
                count += 1
                break
        if curr_char == "(":
            if i != ')':
                count += 1
                break
        if curr_char == "[":
            if i != ']':
                count += 1
                break
if count > 0:
    print("NO")
else:
    print("YES")


# or like that

expression = input()
stack = []

for i in expression:
    if i in ['(', '[', '{']:
        stack.append(i)
    elif i in [')', ']', '}']:
        if not stack:
            print("NO")
            break
        curr_symbol = stack.pop()
        if (i == ')' and curr_symbol != '(') or \
           (i == ']' and curr_symbol != '[') or \
           (i == '}' and curr_symbol != '{'):
            print("NO")
            break

else:
    if not stack:
        print("YES")
    else:
        print("NO")
