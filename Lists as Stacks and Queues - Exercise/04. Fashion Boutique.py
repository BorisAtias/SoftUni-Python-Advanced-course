box_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

rack_stak = []
racks_count = 1
while box_of_clothes:

    if not rack_stak:
        rack_stak.append(box_of_clothes.pop(-1))
    else:
        if sum(rack_stak) + box_of_clothes[-1] > rack_capacity:
            del rack_stak[::]
            rack_stak.append(box_of_clothes.pop(-1))
            racks_count += 1
        else:
            rack_stak.append(box_of_clothes.pop(-1))

print(racks_count)
