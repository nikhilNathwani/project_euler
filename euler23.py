import time
from sets import Set
import math
import itertools
from collections import Counter

start= time.time()
abundNums= []
pairSums= Set([])

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

def sumOfProperDivisors(num,roots):
	lst= Counter(roots).items()
	prod= 1
	for prime,exp in lst:
		prod *= ((prime**(exp+1))-1)/(prime-1)
	return prod-num


def getAllFactors(num,roots):
	factors=[1]
	currProd= 1
	for r in range(1,(1+len(roots)/2)):
		for setcombo in set(itertools.combinations(roots, r)):
			for val in setcombo:
				currProd *= val
			factors += [currProd, num/currProd]
			currProd= 1
	return set(factors)

def isAbundant(num):
	roots= getPrimeRoots(num)
	#return sumOfProperDivisors(num,roots)>num
	factors= getAllFactors(num,roots)
	return sum(factors)>num


for i in range(1,28124):
	if sumOfProperDivisors(i,getPrimeRoots(i))>i:
		abundNums += [i]
		for num in abundNums:
			pairSums.add(i+num)


allNums= Set(range(1,28124))-pairSums

print "Answer:", sum(allNums), max(allNums), min(abundNums)
print "Time taken:", time.time()-start