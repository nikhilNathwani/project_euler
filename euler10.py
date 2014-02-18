import time
import math

primes=[2]

def isPrime(num):
	sqrt= math.sqrt(num)
	for elem in primes:
		if num%elem==0: 
			return False
		if elem>sqrt:
			return True
	return True

def sumOfPrimesUnder(n):
	global primes
	curr= 3
	total=2
	while curr<n:
		#print curr, len(primes)
		if isPrime(curr):
			print curr,total
			total+=curr
			primes += [curr]
		curr += 2
	return int(total),sum(primes)

if __name__=="__main__":
	N= input("Find sum of primes below N. N=")
	start= time.time()
	print "Sum:",sumOfPrimesUnder(N)
	print "Time taken:", time.time()-start

