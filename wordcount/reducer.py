#!/usr/bin/python
"""
Berikut adalah code pada reducer yang digunakan untuk melakukan transformasi data.
<kata1, 1> <kata1, 1> <kata2, 1> menjadi <kata1 sum(1,1)> <kata2, sum(1)>
"""
import sys

#kata terakhir yang sedang diproses
lastkey = None
#sum sementara dari kata $lastkey
current = 0

#Untuk tiap data pada stream
for line in sys.stdin:
    #strip line untuk menghilangkan whitespace
    line = line.strip()
    #split line untuk mendapatkan <kata, 1>
    key, value = line.split('\t')
    try:
        #rubah nilai value dari tipe data string ke int
        value = int(value)
        #apabila yang diproses merupakan kata baru maka
        if key != lastkey:
            #apabila kata lama bukan null
            if lastkey is not None:
                #keluarkan hasil <kata, sum(value)>
                print ('%s\t%d' % (lastkey, current))
            #update kata yang diproses
            lastkey = key
            #inisialisasi nilai sum sementara kembali menjadi 0
            current = 0
        #updaye nilai sum sementara
        current += 1
    except ValueError:
        pass
    
#keluarkan hasil kata yang terakhir kali diproses
if lastkey is not None:
    print ('%s\t%d' % (lastkey,current))