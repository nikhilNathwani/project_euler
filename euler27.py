import time
import math

#facts utilized:
#1) b must be prime
#2a) a+b must be >0 (otherwise result is negative for n=1)
#2b) a>0 and b>0 (follows from 2a)
#3) a must be odd (otherwise n^2 + an + b is even, thus not prime)

start= time.time()
primes=[2]

def isPrime(num):
	if num<=1: return False
	if num in primes: return True
	sqrt= math.sqrt(num)
	for elem in primes:
		if num%elem==0: 
			return False
		if elem>sqrt:
			return True
	return True


def genPrimesUnder(n):
	global primes
	curr= 3
	while curr<n:
		if isPrime(curr):
			primes += [curr]
		curr += 2


def consecPrime(num0,num1):
	value= 2
	maxSeqLen= -1
	bestMults= -1
	mults= [(1,1),(1,-1),(-1,1)]
	for entry,(mult1,mult2) in enumerate(mults):
		a= mult1*num0; b= mult2*num1
		if a+b>0:
			#print a,b, isPrime(2)
			n= 0
			seqLen= -1
			while isPrime(value):
				#print a,b,seqLen
				value= n**2 + a*n + b
				seqLen += 1
				n += 1
			if seqLen > maxSeqLen:
				maxSeqLen= seqLen
				bestMults= mults[entry]
			value=2
	return bestMults[0]*num0, bestMults[1]*num1, maxSeqLen

genPrimesUnder(1000)
maxConsec= 0; maxA= 0; maxB= 0
for b in primes:
	for a in range(1,1000,2):
		coeff,const,consec= consecPrime(a,b)
		#print consec,maxConsec
		if consec > maxConsec:
			maxA= coeff
			maxB= const
			maxConsec= consec

print "Answer:", maxA*maxB#, maxA, maxB, maxConsec
print "Time taken:", time.time()-start