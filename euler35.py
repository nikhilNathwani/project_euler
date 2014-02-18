import time
import math

primes=[] #try making primes a boolean array

def isPrime(num):
	sqrt= math.sqrt(num)
	for elem in primes:
		if elem>sqrt: #this "if" must come first, or else 2 is excluded
			return True
		if num%elem==0: 
			return False
	return True

def getPrimesUnder(n):
	global primes
	primes += [2]
	curr= 3
	while curr<n:
		if isPrime(curr):
			primes += [curr]
		curr += 2

def rotationsArePrime(num):
	if num==2 or num==5: return True
	for x in ['2','4','6','8','0','5']:
		if x in str(num): 
			return False
	digits= map(int,str(num))
	for i in range(len(digits)):
		tens= len(digits)-1; rot= 0
		#PROUD OF THIS! Clever way to get the rotations of a list!!!!!!!!
		for dig in digits[-i:]+digits[:-i]:
			rot += dig*(10**tens)
			tens -= 1
		if not isPrime(rot):
			return False
	return True


if __name__=="__main__":
	start= time.time()
	getPrimesUnder(1000000)
	numCircularPrimes= 0
	for prime in primes:
		if rotationsArePrime(prime):
			numCircularPrimes += 1
	print "Answer:", numCircularPrimes
	print "Time taken:", time.time()-start