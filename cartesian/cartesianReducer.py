#!/home/ubuntu/anaconda3/bin/python

import sys
current_key = None
current_sum = 0
for kv in sys.stdin:
    key, value = kv.split(" ")
    value = int(value)
    if current_key == key :
        current_sum *= value
    elif current_key != key:
        if current_key is not None:
            print("%s %d" % (current_key, current_sum))
        current_key = key
        current_sum = value
print("%s %d" % (current_key, current_sum))
