#!usr/bin/python3
import sys

result = 0
prev_depth = int(input())

for name in sys.stdin:
    curr_depth = int(name.rstrip())

    if curr_depth > prev_depth:
        result += 1

    prev_depth = curr_depth

print(result)