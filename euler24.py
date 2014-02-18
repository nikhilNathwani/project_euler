import itertools
import time

start=time.time()
perms= itertools.permutations(range(10))
count= 1
answer= []
for p in perms:
	if count==1000000:
		answer= p
		break
	count += 1

print "Answer:", int(''.join(map(str,answer)))
print "Time taken:", time.time()-start

#second way:
print "Doing it another way..."
start=time.time()

def getPermutations(a):
   if len(a)==1:
      yield a
   else:
      for i in range(len(a)):
         this = a[i]
         rest = a[:i] + a[i+1:]
         for p in getPermutations(rest):
            yield [this] + p

index = 0
for k in getPermutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    index += 1
    if index == 1000000:
        print "Answer:", int(''.join(map(str,k)))
        break
print "Time taken:", time.time()-start