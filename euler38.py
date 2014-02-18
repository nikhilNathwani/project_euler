import time
import math


def hasUniqueOneToNine(num1,num2):
	string= str(num1)+str(num2)
	return '0' not in string and len(string)==len(set(list(string)))==9  

start= time.time()
numsToCheck= range(9000,10000)
pandigs= []

for n in numsToCheck:
	if hasUniqueOneToNine(n,2*n):
		pandigs += [str(n)+str(2*n)]

print "Answer:", pandigs[-1]
print "Time taken:", time.time()-start