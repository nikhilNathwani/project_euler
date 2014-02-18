import time

start= time.time()
pandigitals= []

#instead of using set, could use boolean array!!! probably faster?

def hasUniqueOneToNine(a,b,ab):
	string= str(a)+str(b)+str(ab)
	return '0' not in string and len(string)==len(set(list(string)))==9  

for a in range(1,100):
	for b in range(100,10000):
		if hasUniqueOneToNine(a,b,a*b):
			pandigitals += [a*b]

print "Answer:", sum(set(pandigitals))
print "Time taken:", time.time()-start