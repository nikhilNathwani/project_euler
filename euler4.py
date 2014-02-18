import time

def isPalindrome(num):
	word= str(num)
	return len(word)<=1 or (word[0]==word[-1] and isPalindrome(word[1:-1]))

#throwing all palindromes into an array and then taking the max is
#just as fast as locally keeping track of the largest seen palidrome 
#and updating when necessary. It is, of course, more memory-intensive
def findLargestPal():
	largest= -1
	for x in range(999,99,-1):
		for y in range(999,99,-1):
			#due to lazy evaluation, program runs ~8.5 times faster 
			#when x*y>largest comes before isPalindrome(x*y)!
			if x*y>largest and isPalindrome(x*y):
				largest= x*y
	return largest

if __name__=="__main__":
	start= time.time()
	print "Answer:", findLargestPal()
	print "Time taken:", time.time()-start