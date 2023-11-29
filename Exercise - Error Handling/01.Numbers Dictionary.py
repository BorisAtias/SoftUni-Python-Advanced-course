# The task is being written in two ways due to uncertainty how much we are allowed to alter the code provided!

# 1. Numbers Dictionary - First way

num_dict = {}

while True:
    line = input()

    if line == "Search":
        break

    num_as_str = line

    try:
        number = int(input())
        num_dict[num_as_str] = number
    except ValueError:
        print("The variable number must be an integer")

while True:
    line = input()

    if line == "Remove":
        break

    searched = line

    try:
        print(num_dict.get(searched, "Number does not exist in dictionary"))
    except KeyError:
        print("Number does not exist in dictionary")

while True:
    line = input()

    if line == "End":
        break

    searched = line

    try:
        del num_dict[searched]
    except KeyError:
        print("Number does not exist in dictionary")

print(num_dict)


# Second way, where I kept the original structure!


num_dict = {}

line = input()

while line != "Search":

    num_as_str = line

    try:
        number = int(input())
        num_dict[num_as_str] = number
    except ValueError:
        print("The variable number must be an integer")
        line = input()
        continue
    line = input()



line = input()

while line != "Remove":

    searched = line

    try:
        print(num_dict[searched])
    except KeyError:
        print("Number does not exist in dictionary")
        line = input()
        continue
    line = input()

line = input()

while line != "End":

    searched = line

    try:
        del num_dict[searched]
    except KeyError:
        print("Number does not exist in dictionary")
        line = input()
        continue
    line = input()

print(num_dict)

