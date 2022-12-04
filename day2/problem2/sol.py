#!/bin/env python3
with open("input.txt") as f:
    data = f.readlines()

WON = 6
DRAWN = 3
LOST = 0

total_points = 0
for line in data:
    opponent, result = line.strip().split(" ")
    opponent = ord(opponent) - ord('A')
    if result == "X":
        round_points = LOST + (opponent - 1)%3 + 1
    elif result == "Y":
        round_points = DRAWN + opponent + 1
    elif result == "Z":
        round_points = WON + (opponent + 1)%3 + 1

    total_points += round_points
    # print(line, result, opponent, round_points)

print(total_points)