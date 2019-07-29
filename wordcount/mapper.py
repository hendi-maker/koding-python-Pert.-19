#!/usr/bin/python
"""
Berikut adalah code pada mapper yang digunakan untuk melakukan transformasi data.
<kata1 kata2 kata3> menjadi <kata1, 1> <kata2, 1> <kata3, 1>
"""
#import lybrary sys untuk mendapatkan stream input dari Hadoop
import sys

#Untuk tiap data pada stream
for line in sys.stdin:
    #strip line untuk menghilangkan whitespace
    line = line.strip()
    #split line untuk mendapatkan <kata> <kata> <kata> dari <kata kata kata>
    words = line.split()
    #untuk setiap kata
    for word in words:
        #keluarkan hasil <kata,1> <kata,1> <kata,1>
        print ('%s\t%d' % (word, 1))