#!/home/ubuntu/anaconda3/bin/python

import sys

current_key = "0"
current_sum = 0
for line in sys.stdin:
    key, value = line.split(" ")
    if key == current_key :
        current_sum += int(value)
    else:
        print(current_sum)
        current_key=key
        current_sum = int(value)
print(current_sum)
