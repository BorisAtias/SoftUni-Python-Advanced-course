guest_count = int(input())

regular_guest = set()
vip_guests = set()
guests_who_came = []

for i in range(guest_count):

    reservation_code = input()
    if reservation_code[0].isnumeric():
        vip_guests.add(reservation_code)
    else:
        regular_guest.add(reservation_code)

while True:

    guest = input()
    if guest == "END":
        break
    guests_who_came.append(guest)

vip_not_attend = []
regular_not_attend = []

for guest in vip_guests:
    if guest not in guests_who_came:
        vip_not_attend.append(guest)

for guest in regular_guest:
    if guest not in guests_who_came:
        regular_not_attend.append(guest)

vip_not_attend.sort()
regular_not_attend.sort()

print(f'{len(vip_not_attend) + len(regular_not_attend)}')

for guest in vip_not_attend:
    print(guest)

for guest in regular_not_attend:
    print(guest)