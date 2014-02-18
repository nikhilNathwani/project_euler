import time

knowns= {}

N= int(input("Find number under N with longest Collatz sequence. N="))
initTime= time.time()
maxVal= -1; maxStart= 0
for i in range(1,N):
	start= i; origStart= i
	count= 1
	while start != 1:
		if start<origStart: #slightly faster than "if start in knowns:
			count += knowns[start]
			break
		if start%2 == 0:
			start /= 2
		else: 
			start= 1+(3*start)
		count += 1
	if count > maxVal: 
		maxVal= count
		maxStart= i
	knowns[i]= count

print "Number w/ longest seq=", maxStart
print "Time taken", time.time()-initTime