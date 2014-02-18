from sets import Set
import time 

start= time.time()
powers= Set([])

#for a in range(2,101):
#	for b in range(2,101):
#		powers.add(a**b)
#print "Answer:", len(powers)

#alternative:
print "Answer:", len(set([a**b for a in range(2,101) for b in range(2,101)]))
print "Time taken:", time.time()-start