#!/home/ubuntu/anaconda3/bin/python

import sys

for line in sys.stdin:
    value = int(line)
    key = 0 if value % 2 == 0 else 1
    print ("%d %d" % (key, value))
