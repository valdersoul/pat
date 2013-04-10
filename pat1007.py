def generateP( num , n ):
	for x in range(num+1, 2*n):
		if ( isP(x)):
			return x
			break

def isP( m ):
	n = pingfang(m)
	if( m == 2 or m == 3):
		return 1
	else :
		#y = 0
		for x in range(2, n+1 ):
			if ( (m % x) == 0):
				return 0
			'''else :
				y = x'''
		if ( x == n ):
			return 1

def pingfang( shuzi ):
	x= float(shuzi)
	y= sqrt(x)
	return int(y)
	pass


import time
from math import sqrt
number = int( input() )
starttime = time.clock()
count = 0 
p1 = 2
p2 = 3
while ( p2 <= number ):
	if ( (p2 - p1) == 2):
		count += 1
	p1 = p2
	p2 = generateP(p2 , number)
else :
	print(count)
endtime = time.clock()
print(endtime - starttime)