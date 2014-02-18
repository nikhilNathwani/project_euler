import time
import math
import itertools

amicables= {}
amicablePairs= []

def getPrimeRoots(num):
	if num==2: return [2]
	roots=[]
	low=2; upp= num #low should always be >=2, never 1 (b/c that'd skip 2)
	while upp>1:
		if upp%low==0:
			roots += [low]
			upp /= low
		else: 
			if low==2: low+=1
			else: low+=2
		if low > math.sqrt(upp):
			roots += [int(upp)]
			break
	return roots

def getAllFactors(roots):
	factors=[1]
	currProd= 1
	for r in range(1,(1+len(roots)/2)):
		for setcombo in set(itertools.combinations(roots, r)):
			for val in setcombo:
				currProd *= val
			factors += [currProd, num/currProd]
			currProd= 1
	return set(factors)

def addAmicablePair(num,factors):
	global amicables, amicablePairs
	factorSum= sum(factors)
	amicables[factorSum]= num
	if num != factorSum and num in amicables and amicables[num]==factorSum:
		amicablePairs += [num,factorSum]

if __name__=="__main__":
	start= time.time()
	for num in range(1,10000):
		roots= getPrimeRoots(num)
		factors= getAllFactors(roots)
		addAmicablePair(num,factors)
	print "Sum of all amicable numbers:", sum(amicablePairs)
	print "Time taken:", time.time()-start