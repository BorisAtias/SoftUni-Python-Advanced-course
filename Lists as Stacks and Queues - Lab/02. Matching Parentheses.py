def extract_parentheses(equation):
    stack = []
    results = []

    for i, char in enumerate(equation):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                start = stack.pop()
                results.append(equation[start:i + 1])

    return results

equation = input()


parentheses = extract_parentheses(equation)
for i, p in enumerate(parentheses):
    print(f"{p}")
