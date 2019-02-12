# Farkle

import random

# roll Nd6
def roll(n):
    return list(random.randint(1,6) for i in range(n))

p1_score = 0
p2_score = 0
turn = 1
while p1_score < 10000 and p2_score < 10000:
    print("Player", turn, "'s turn.")
    dice = roll(6)
    dice.sort()
    print("Pos. 0 1 2 3 4 5")
    print("Val.", " ".join(str(i) for i in dice))
    # dummy line
    a = input()

    # change turn
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1
