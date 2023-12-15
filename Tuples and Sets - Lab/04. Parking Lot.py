car_count = int(input())

parking_lot = {}

for _ in range(car_count):

    cars = input().split(", ")
    command, car = cars[0], cars[1]
    if command == "IN":
        parking_lot[car] = car
    elif command == "OUT":
        if car in parking_lot:
            del parking_lot[car]

if not parking_lot:
    print("Parking Lot is Empty")
else:
    for car in parking_lot:
        print(car)

# Using Sets

n = int(input())
parking_lot = set()

for _ in range(n):
    direction, car_number = input().split(", ")

    if direction == "IN":
        parking_lot.add(car_number)
    elif direction == "OUT" and car_number in parking_lot:
        parking_lot.remove(car_number)

if parking_lot:
    print("\n".join(parking_lot))
else:
    print("Parking Lot is Empty")

