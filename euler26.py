import time
import math

primes=[2]
start= time.time()

def isPrime(num):
	sqrt= math.sqrt(num)
	for elem in primes:
		if num%elem==0: 
			return False
		if elem>sqrt:
			return True
	return True

def primesUnder(n):
	global primes
	curr= 3
	while curr<n:
		#print curr, len(primes)
		if isPrime(curr):
			primes += [curr]
		curr += 2

def repeatedNineMultiple(num):
	nineMult= 9
	count= 0
	while nineMult%num != 0:
		count += 1
		nineMult += 9*(10**count)
	return nineMult, count+1


primesUnder(1000)
maxRepeat= 0; maxRepeatNum= 0
primes.remove(2); primes.remove(5) #can't have divisors of 10
for p in primes: 
	n,reps= repeatedNineMultiple(p)
	if reps>maxRepeat:
		maxRepeat= reps
		maxRepeatNum= p

print "Answer:", maxRepeatNum
print "Time taken:", time.time()-start
