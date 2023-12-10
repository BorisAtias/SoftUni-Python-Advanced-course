from collections import deque

robots = input().split(";")
start_time = input().split(":")
start_time = f'{int(start_time[0]):02d}:{start_time[1]}:{start_time[2]}'

robots_info = {}
products = deque()
end_production = False


def time(curr_time):
    curr_time = curr_time.split(":")
    hour, minutes, seconds = int(curr_time[0]), int(curr_time[1]), int(curr_time[2])
    if seconds + 1 == 60:
        seconds = 0
        minutes += 1
        if minutes + 1 == 60:
            minutes = 0
            hour += 1
            if hour + 1 == 24:
                hour = 0
                minutes = 0
                seconds = 0
    else:
        seconds += 1

    result = f"{int(hour)}:{float(minutes)}:{float(seconds)}"
    return result

def available_robot(curr_time, processing_time):
    curr_time = curr_time.split(":")
    hour, minutes, seconds = int(curr_time[0]), int(curr_time[1]), int(curr_time[2])
    if seconds + processing_time >= 60:
        seconds = processing_time - 60
        minutes += 1
    else:
        seconds += processing_time

    result = f"{hour:02d}:{minutes:02d}:{seconds:02d}"
    return result


for robot in robots:
    name, processing_time = robot.split("-")
    robots_info[name] = [int(processing_time), start_time]

details = input()
products.append(details)
curr_time = start_time

while products:
    curr_time = time(curr_time)

    for robot, value in robots_info.items():
        if curr_time >= robots_info[robot][1]:
            print(f"{robot} - {details} [{curr_time[0::]}]")
            robots_info[robot][1] = available_robot(start_time, robots_info[robot][0])
            products.popleft()
            break
        else:
            continue


    if not end_production:
        details = input()
    else:
        continue
    if details == "End":
        end_production = True
        continue
    products.append(details)
    products.rotate(1)

"""
ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End

"""