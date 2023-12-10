petrol_pumps_number = int(input())
tank = 0
current_tank = 0
station_position = 0
pumps = []
for i in range(petrol_pumps_number):

    petrol_in_pump, distance_next_pump = map(int, input().split())
    pumps.append((petrol_in_pump, distance_next_pump))

for i in range(len(pumps)):
    petrol_in_pump, distance_next_pump = pumps[i]
    current_tank += petrol_in_pump - distance_next_pump
    if current_tank < 0:
        station_position = i + 1
        current_tank = 0

    tank += petrol_in_pump
if tank < sum(pump[1] for pump in pumps):
    station_position = -1

print(station_position)


# second way


def find_starting_petrol_pump(petrol_pumps):
    n = len(petrol_pumps)
    start = 0
    current_petrol = 0
    tank = 0

    for i in range(n):
        petrol_in_pump, distance_next_pump = petrol_pumps[i]
        current_petrol += petrol_in_pump - distance_next_pump

        if current_petrol < 0:
            start = i + 1
            current_petrol = 0

        tank += petrol_in_pump

    if tank >= 0:
        return start
    else:
        return -1

def main():
    n = int(input())
    petrol_pumps = []

    for i in range(n):
        petrol, distance = map(int, input().split())
        petrol_pumps.append((petrol, distance))

    starting_pump = find_starting_petrol_pump(petrol_pumps)

    if starting_pump != -1:
        print(f"{starting_pump}")


if __name__ == "__main__":
    main()

