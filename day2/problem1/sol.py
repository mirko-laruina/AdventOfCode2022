#!/bin/env python3
with open("input.txt") as f:
    data = f.readlines()

WON = 6
DRAWN = 3
LOST = 0

win_matrix = [
    [ DRAWN,    LOST,   WON     ],
    [ WON,      DRAWN,  LOST    ],
    [ LOST,     WON,    DRAWN   ]
]

total_points = 0
for line in data:
    opponent, me = line.strip().split(" ")
    me = ord(me) - ord('X')
    opponent = ord(opponent) - ord('A')
    round_points = win_matrix[me][opponent] + (me + 1)
    total_points += round_points
    # print(line, me, opponent, round_points)

print(total_points)