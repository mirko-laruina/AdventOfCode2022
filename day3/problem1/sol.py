#!/bin/env python
with open("input.txt") as f:
    lines = f.readlines()

pts = 0
ord_a = ord('a')
ord_A = ord('A')
for line in lines:
    line = line.strip()
    half_length = len(line)//2
    first = line[:half_length]
    second = line[half_length:]
    common_elem = set(first).intersection(set(second)).pop()
    if(common_elem >= 'a'):
        pts += ord(common_elem) - ord_a + 1
    else:
        pts += ord(common_elem) - ord_A + 27
    print(first, second, common_elem)

print(pts)