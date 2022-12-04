#!/bin/env python
with open("input.txt") as f:
    lines = f.readlines()

pts = 0
ord_a = ord('a')
ord_A = ord('A')


common_set = set()
for i, line in enumerate(lines):
    line = line.strip()
    if i % 3 == 0:
        common_set = set(line)
    else:
        common_set = set(common_set).intersection(line)

    if(i % 3 == 2):
        common_elem = common_set.pop()
        ord_common_elem = ord(common_elem)
        if(ord_common_elem >= ord_a):
            pts += ord_common_elem - ord_a + 1
        else:
            pts += ord_common_elem - ord_A + 27
        common_set = set()

print(pts)