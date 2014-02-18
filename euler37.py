import time
import math

primes=[0,0,1] #try making primes a boolean array
truncs= []

def isPrime(num):
	sqrt= math.sqrt(num)
	for (i,elem) in enumerate(primes):
		if elem:
			if i>sqrt: #this "if" must come first, or else 2 is excluded
				return True
			if num%i==0: 
				return False
	return True

def checkTrunc(num):
	global truncs
	digs= 1+int(math.log10(num))
	tmp= num
	#right to left truncation
	for i in range(1,digs):
		tmp /= 10
		if not primes[tmp]:
			return False
	#left to right truncation
	for i in range(1,digs):
		tmp= num
		if not primes[tmp%(10**i)]:
			return False
	print num
	return True


start= time.time()
curr=3
while len(truncs)<11:
	if isPrime(curr):
		primes += [1,0]
		if len(str(curr))>1 and checkTrunc(curr):
			truncs += [curr]
	else:
		primes += [0,0]
	curr += 2

print "Truncatable primes:", truncs
print "Sum:", sum(truncs)
print "Time taken:", time.time()-start