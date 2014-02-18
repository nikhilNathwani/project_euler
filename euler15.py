import math
import time

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

N= input("Square grid sidelength=")
start= time.time()
#Any path requres 2N moves: N rightward and N downward
#A path is uniquely determined by the placement of the N rightward moves
#So, there are 2N choose N possible paths
print "Answer:", nCr(2*N,N)
print "Time taken:", time.time()-start
