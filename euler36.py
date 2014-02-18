import time
import math

palindromesDigs= [['0','1','2','3','4','5','6','7','8','9'],['00','11','22','33','44','55','66','77','88','99']]
oddPals= [1,3,5,7,9,11,33,55,77,99]

#n must be at least 3 digits
def genAllPalindromesUnder(n):
	global palindromesDigs, oddPals
	numDigs= int(math.log10(n))
	for i in range(3,numDigs+1):
		palindromesDigs += [[]]
		for wrap in map(str,range(10)):
			for prev in palindromesDigs[i-3]:
				digsToAdd= wrap+prev+wrap
				palindromesDigs[i-1] += [digsToAdd]
				if int(wrap)%2==1:
					oddPals += [int(digsToAdd)]

def isPalidrome(binString):
	if len(binString) <= 1: 
		return True
	return binString[0]==binString[-1] and isPalidrome(binString[1:-1])

start= time.time()
genAllPalindromesUnder(1000000)
doubleBasePals= []
doubleBasePalSum= 0 
for oddPal in oddPals:
	if isPalidrome(bin(oddPal)[2:]):
		doubleBasePals += [(oddPal, bin(oddPal)[2:])]
		doubleBasePalSum += oddPal

#print doubleBasePals
print "Answer:", doubleBasePalSum
print "Time taken:", time.time()-start

