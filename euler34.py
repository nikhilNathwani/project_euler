import time
import math

start= time.time()

#THE TRICK IS TO PRECALCULATE THE FACTORIALS! DUH!!!!
digitFactorials= []
facts= [1,1,2,6,24,120,720,5040,40320,362880]

#finding max num of digits
digAmt= 2

while digAmt*(facts[9]) >= 10**(digAmt-1):
	digAmt += 1

for i in xrange(10,digAmt*(facts[9])):
	digSum= 0
	for dig in str(i):
		digSum += facts[int(dig)]
	if digSum==i:
		digitFactorials += [i]

print "Answer:",sum(digitFactorials)
print "Time taken:", time.time()-start

def findFact():
   facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
   limit = 362880 * 9
   for i in xrange(0, limit):
      total = 0
      stringI = str(i)
      for j in stringI:
         total += facts[int(j)]
      if (total == i):
         print i

'''if __name__=="__main__":
	start= time.time()
	findFact()
	print time.time()-start'''

