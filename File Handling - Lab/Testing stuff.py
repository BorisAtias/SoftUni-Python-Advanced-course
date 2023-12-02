import os

# Save data providing file in same directory

"""email = input()

file = open("users.txt", "a")
file.write(email + "\n")
file.close()"""


# Save data providing file another directory using uni_path

"""my_working_dir = os.path.dirname(os.path.abspath(__file__)) # Find the absolute path
print(my_working_dir)

file_path = my_working_dir + "/Test - lab/boris.txt"

email = input()
file = open(file_path, "w")
file.write(email + "\n")
file.close()"""


# Using join() makes sure eliminates the differences between the OS used from client and user

"""my_working_dir = os.path.dirname(os.path.abspath(__file__))
print(my_working_dir)

file_path = os.path.join(my_working_dir, "Test - Lab", "boris.txt")

email = input()
file = open(file_path, "w")
file.write(email + "\n")
file.close()"""

# File Handling with Error Handling
"""
try:
    file = open("invalid.txt", "r")
except FileNotFoundError:
    print("File not found or path is incorrect")
"""

# Testing

my_working_dir = os.path.dirname(os.path.abspath(__file__))
print(my_working_dir)

file_path = os.path.join(my_working_dir, "Test - Lab", "boris.txt")

"""#email = input()
file = open(file_path, "w")
file.writelines(["a\n", "b\n", "c\n"])
file.close()"""


# CLOSING FILES AUTOMATICALLY when the block of code is executed!!!

with open(file_path, "w") as f:
    f.write("Hello Boris")


# More testing


file_path = input("Please enter file path: ")

try:
    with open(file_path, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Invalid path was given")