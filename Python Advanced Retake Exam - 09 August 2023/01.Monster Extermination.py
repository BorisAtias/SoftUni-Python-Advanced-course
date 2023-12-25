from collections import deque

monster_armor_sequence = deque([int(x) for x in input().split(",")])
soldier_attack = [int(x) for x in input().split(",")]
monsters_killed = 0

while monster_armor_sequence and soldier_attack:

    monster = monster_armor_sequence.popleft()
    soldier = soldier_attack.pop()

    if soldier >= monster:
        monsters_killed += 1
        soldier -= monster
        if soldier_attack:
            soldier_attack[-1] += soldier
        elif not soldier_attack and soldier > 0:
            soldier_attack.append(soldier)
    else:
        monster -= soldier
        monster_armor_sequence.append(monster)

if not monster_armor_sequence:
    print("All monsters have been killed!")
if not soldier_attack:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {monsters_killed}")


#--------------------------------------------#

from collections import deque

def simulate_battle(monster_armor_sequence, soldier_attack):
    killed_monsters = 0

    while monster_armor_sequence and soldier_attack:
        monster = monster_armor_sequence.popleft()
        soldier = soldier_attack.pop()

        if soldier >= monster:
            killed_monsters += 1
            soldier -= monster

            if soldier_attack:
                soldier_attack[-1] += soldier
            else:
                if soldier > 0:
                    soldier_attack.append(soldier)
        else:
            monster -= soldier
            monster_armor_sequence.append(monster)

    if not monster_armor_sequence:
        print("All monsters have been killed!")
    if not soldier_attack:
        print("The soldier has been defeated.")
    print(f"Total monsters killed: {killed_monsters}")


monster_armor_sequence = deque(map(int, input().split(",")))
soldier_attack = deque(map(int, input().split(",")))

simulate_battle(monster_armor_sequence, soldier_attack)
