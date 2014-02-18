import time
nums= []

start= time.time()
with open("largenums.txt") as f:
	for line in f:
		nums += [int(line.strip())]

val=sum(nums)
while val != val%(10**10):
	val /= 10

print "Last 10 digits:", val
print "Time taken:", time.time()-start