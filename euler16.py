#!/usr/bin/python

import time

start=time.time()
sum= 0
for char in str(2**1000):
	sum += int(char)
print "Digit sum of 2^1000=", sum
print "Time taken", time.time()-start