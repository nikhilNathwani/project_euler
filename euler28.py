import time

#did it in (effectively) one line!

#the corners of each outer square adds n^2,n^2-k,n^2-2k, and n^2-3k, where k=n-1
#so, each outer square adds 4n^2-6k= 4n^2-6n+6 where n is the number of rows 
#so, answer is 1 + sum from 3 to n (increments of 2) of 4n^2-6n+6, when n is number of rows
#since n is always odd, our summation skips terms. Let k=index of outer square, then n=2k+1
#now its 1 + sum from 1 to k of 16k^2+4k+4,
#by summation formulas, this is 16k(k+1)(2k+1)/6 + 4k(k+1)/2 + 4k + 1

k= (input("Number of rows? Must be odd:")-1)/2
start=time.time()
answer= 8*k*(k+1)*(2*k+1)/3 + 2*k*(k+1) + 4*k + 1

print "Answer:", answer
print "Time taken:", time.time()-start