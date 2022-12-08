#!/bin/env python3

# Part one
# WINDOW_SIZE = 4


# Part two
WINDOW_SIZE = 14


def get_skippable_idx(window):
    for i, char_i in enumerate(window):
        for j, char_j in enumerate(window[i+1:]):
            if char_i == char_j:
                return i+1
    return 0

# Processes the window in reverse, faster
def get_skippable_idx_rev(window):
    i = WINDOW_SIZE - 1
    while i > 0:
        for j, char_j in enumerate(window[i-1::-1]):
            if window[i] == char_j:
                return i - j
        i -= 1
    return 0

with open("input.txt") as f:
    signal = f.readline()


i = WINDOW_SIZE
it_count = 0
sig_len = len(signal)
while(i < sig_len):
    window = signal[i - WINDOW_SIZE:i]
    skip_idx = get_skippable_idx_rev(window)
    if skip_idx == 0:
        break
    it_count += 1
    i += skip_idx

print("Iterations:", it_count)
print("First unique pattern at:", i)