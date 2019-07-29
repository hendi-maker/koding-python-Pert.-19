#!/home/ubuntu/anaconda3/bin/python

import sys
with open("counter",'r') as c:
    data_count = int(c.read())

counter = 1
for value in sys.stdin:
    value = int(value)
    for i in range(data_count):
        print("(%d,%d) %d" % (counter, i+1, value))
        print("(%d,%d) %d" % (i+1, counter, value))
    counter +=1
