import time

start= time.time()

monthDays= {0:31,1:28,2:31,3:30,4:31,5:30,6:31,7:31,8:30,9:31,10:30,11:31}
year=1900
day= -1
currMonth= 0
numInitSundays= 0

while year!=1901:
	daysForCurrMonth= monthDays[currMonth]
	if currMonth==1 and year%4==0 and not(year%100==0 and year%400!=0):
		daysForCurrMonth=29
	for i in range(daysForCurrMonth):
		day += 1
	if currMonth==11:
		year+=1
	currMonth= ((currMonth+1)%12)

while year!=2001:
	daysForCurrMonth= monthDays[currMonth]
	if currMonth==1 and year%4==0 and not(year%100==0 and year%400!=0):
		daysForCurrMonth=29
	if day%7==5: 
		print "woop",day%7,currMonth,year
		numInitSundays+=1
	for i in range(daysForCurrMonth):
		day += 1
	if currMonth==11:
		year+=1
	currMonth= ((currMonth+1)%12)
	#print currMonth,day

print "Answer:", numInitSundays
print "Time taken:", time.time()-start
