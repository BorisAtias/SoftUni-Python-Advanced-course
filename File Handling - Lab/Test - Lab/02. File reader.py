import os

my_working_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(my_working_dir, "numbers.txt")

file = open(file_path, "r")

total = 0
for line in file:
    curr_num = int(line)
    total += curr_num

file.close()
print(total)