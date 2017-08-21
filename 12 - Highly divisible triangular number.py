from math import *
from time import *
from prime import *
from number_factors import *


sum = 0
i = 1

start = clock()


while True:
	sum = sum+i
	if (len(factors(sum)) >= 500):
		print factors(sum)
		break
	i += 1
print sum
	
print clock() - start
