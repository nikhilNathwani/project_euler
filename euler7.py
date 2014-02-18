import time
import math
primes= [2]

def isPrime(num):
	sqrt= math.sqrt(num)
	for elem in primes:
		if num%elem==0: 
			return False
		if elem>sqrt:
			return True
	return True

def findNthPrime(n):
	global primes
	curr= 3
	while len(primes)<n:
		#print curr, len(primes)
		#print primes, curr
		if isPrime(curr):
			primes += [curr]
		curr += 2
	return primes[-1]

if __name__=="__main__":
	N= input("Find the Nth prime. N=")
	start= time.time()
	print "%dth prime:"%N,findNthPrime(N)
	print "Time taken:", time.time()-start

