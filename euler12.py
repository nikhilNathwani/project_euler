from itertools import groupby
from operator import mul
import math
import sys
import time

def numFactorsAboveThresh(thresh):
	triangNum= 1; count=1
	prod=0
	while prod<500:
		#First getting roots, then calculating number of factors
		roots=[]
		low=2; upp= triangNum #low should always be >=2, never 1 (b/c that'd skip 2)
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
		
		#now getting multiplicities of roots. Multiplying these gives # of factors
		if len(roots)>0:
			multiplicities= [len(list(group))+1 for key, group in groupby(roots)]
			prod= reduce(mul, multiplicities)
			print triangNum, multiplicities, prod
			if prod >= thresh: 
				return triangNum
		count += 1
		triangNum += count

if __name__=="__main__":
	N= input("Find smallest triangular number with N divisors. N=")
	start=time.time()
	print "Answer:", numFactorsAboveThresh(N)
	print "Time taken:", time.time()-start