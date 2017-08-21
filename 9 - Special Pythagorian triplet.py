from math import *
from time import *

start = clock()
flag = 0
for b in xrange(100,500):
	for a in xrange(100,500):
		c = 1000-a-b
		if ((a*a + b*b) == c*c):
			print a*b*c
			flag = 1
			break
	if flag == 1:
		break

print clock() - start