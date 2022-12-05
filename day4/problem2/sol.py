#!/bin/env python3

def is_overlap(first, second):
    if first[1] >= second[0] and first[0] <= second[1]:
        return True

with open("input.txt") as f:
    lines = [ l.strip() for l in f.readlines() ]

count = 0
for line in lines:
    range_first, range_sec = [ [ int(s) for s in r.split("-") ] for r in line.split(",") ]
    # print(range_first, range_sec)
    if is_overlap(range_first, range_sec) or is_overlap(range_sec, range_first):
        count += 1

print(count)
