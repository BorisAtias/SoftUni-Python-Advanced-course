name_count = int(input())

names = {}

for _ in range(name_count):
    name = input()
    names[name] = name

for name in names:
    print(name)