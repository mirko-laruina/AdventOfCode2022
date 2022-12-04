#!/bin/env python3
with open('input.txt') as f:
    data = f.readlines()

count = 0
max_count = 0
for line in data:
    if line.strip() == "":
        if max_count < count:
            max_count = count
        count = 0
    else:
        count += int(line.strip())

# Lazy: check the last elf calories count outside the loop (since there is no end line)
if max_count < count:
    max_count = count

print(max_count)