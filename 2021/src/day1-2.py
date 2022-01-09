#!usr/bin/python3
import sys

result = 0
window = [int(input()) for i in range(3)]
prev_sum = sum(window)

for name in sys.stdin:
    window.append(int(name.rstrip()))
    window.pop(0)

    curr_sum = sum(window)
    if curr_sum > prev_sum:
        result += 1

    prev_sum = curr_sum

print(result)