try:
    file = open("boris.txt", "r")
    print("Found")
    file.close()
except FileNotFoundError:
    print("File not found")
