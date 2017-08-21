from math import *

def prime_range(n):
	x = []
	for i in range(int(floor(sqrt(n)))-1,0,-1):
		if (n%i == 0):
			x.append(i)
	print x
			

prime_range(600851475143)