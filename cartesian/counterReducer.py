#!/home/ubuntu/anaconda3/bin/python

import sys
current_sum=0
for line in sys.stdin:
    current_sum += int(line)
print(current_sum)
