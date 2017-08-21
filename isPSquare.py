from math import *
from sys import maxint



def isPSquare(n):
	if n<0:
		return False
	test = int(sqrt(n))
	return int(test*test) == n
