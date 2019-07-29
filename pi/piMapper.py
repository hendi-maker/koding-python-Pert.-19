#!/home/ubuntu/anaconda3/bin/python

import sys

for value in sys.stdin:
    x , y = list(map(float, value.split()))
    result = 1 if x*x + y*y <= 1 else 0
    print(result)
