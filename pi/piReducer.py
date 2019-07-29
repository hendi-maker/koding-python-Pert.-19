#!/home/ubuntu/anaconda3/bin/python

import sys

current_sum = 0
count = 0
for value in sys.stdin:
    current_sum += int(value)
    count +=1
print(4 * current_sum / count)
