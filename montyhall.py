from random import randint, choice

class Door:
    def __init__(self):
        self.open = False
        self.prize = False

def play_game(first_door, switch_door):
    doors = [Door(), Door(), Door()]
    # Option 1: randint
    index = randint(0, 2)
    winning_door = doors[index]

    # Option 2: choice
    winning_door = choice(doors)

    winning_door.prize = True
    # Alternative: doors[index].prize = True

    chosen_by_player = first_door

    empty_doors = []
    for i in range(len(doors)):
        if i != chosen_by_player and not doors[i].prize:
            empty_doors.append(doors[i])

    choice(empty_doors).open = True

    if switch_door:
        for i in range(len(doors)):
            if i != chosen_by_player and not doors[i].open:
                chosen_by_player = i
                break

    return doors[chosen_by_player].prize

win_total = 0
for i in range(10000):
    if play_game(0, True):
        win_total += 1

print(f"Won {win_total} times.")

