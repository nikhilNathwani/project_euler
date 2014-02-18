import time
import sys

lst= []

#Dynamic Programming! Max route sum at each node of the tree
#is the max over all parents of: 
#      (that node's value)+max_route_sum(parent)

def listify(filename):
	global lst
	with open(filename) as f:
		for line in f:
			nums= line.strip().split()
			nums= [int(elem) for elem in nums]
			lst += [nums]

def calcMaxRouteSum():
	global lst
	for level in range(1,len(lst)):
		for count,elem in enumerate(lst[level]): 
			if count==0:
				lst[level][count] += lst[level-1][count]
			elif count==len(lst[level])-1:
				lst[level][count] += lst[level-1][count-1]
			else: 
				lst[level][count] += max(lst[level-1][count-1], lst[level-1][count])
	return max(lst[-1])



if __name__=="__main__":
	start=time.time()
	listify(sys.argv[1])
	maxSum= calcMaxRouteSum()
	print "Maximum route sum:", maxSum
	print "Time taken:", time.time()-start
