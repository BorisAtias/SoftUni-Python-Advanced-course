count = int(input())

unique_elements = set()

for i in range(count):

    elements = input().split()

    for el in elements:
        unique_elements.add(el)

for element in unique_elements:
    print(element)