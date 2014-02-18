import time
import math
import sys

start= time.time()
roots=[]
low=2; upp= int(sys.argv[1]) #low should always be >=2, never 1 (b/c that'd skip 2)
while upp>1:
	if upp%low==0:
		roots += [low]
		upp /= low
	else: 
		if low==2: low+=1
		else: low+=2
	if low > math.sqrt(upp):
		roots += [int(upp)]
		break

print "Prime roots:", roots
print "Time taken:", time.time()-start