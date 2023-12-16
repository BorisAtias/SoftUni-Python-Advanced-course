user_count = int(input())
users = set()


for i in range(user_count):

    user_name = input()
    users.add(user_name)

for name in users:
    print(name)