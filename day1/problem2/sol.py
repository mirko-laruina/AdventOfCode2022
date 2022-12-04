#!/bin/env python3

MAX_K = 3

with open('input.txt') as f:
    data = f.readlines()

calories_array = []
count = 0
for line in data:
    if line.strip() == "":
        calories_array.append(count)
        count = 0
    else:
        count += int(line.strip())

# Lazy and computationally expensive O(nlogn), could implement a top-K algorithm in O(n)
calories_array = sorted(calories_array)
print(sum(calories_array[-MAX_K:]))