import time
import math

start= time.time()

digitFifthPowers= []

#finding max num of digits
digAmt= 2

while digAmt*(9**5) >= 10**(digAmt-1):
	digAmt += 1

for i in range(10,digAmt*(9**5)):
	digSum= 0
	for dig in str(i):
		digSum += int(dig)**5
	if digSum==i:
		digitFifthPowers += [i]

print "Answer:",sum(digitFifthPowers)
print "Time taken:", time.time()-start






