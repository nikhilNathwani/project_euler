import math
import time

start=time.time()
digSum=0
n= math.factorial(100)
for char in str(n):
	digSum += int(char)

print "Digit sum of 100! is:", digSum
print "Time taken", time.time()-start
