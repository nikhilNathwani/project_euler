import time

start= time.time()

def makeXPound(x,coins):
	if x==0 or x==min(coins): return 1
	elif x < min(coins): return 0
	else: return makeXPound(x-coins[0],coins)+makeXPound(x,coins[1:])

print makeXPound(0, [1,2,5,10,20,50,100,200])
print "Time taken:", time.time()-start