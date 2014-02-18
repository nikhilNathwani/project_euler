import time

start= time.time()
bound= 10**999

fib0=0
fib1=1
count= 1

while fib1 <= bound:
	tmp= fib0
	fib0= fib1
	fib1 += tmp
	count += 1

print "Answer:", count
print "Time taken:", time.time()-start
