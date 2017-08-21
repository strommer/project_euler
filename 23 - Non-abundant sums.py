from math import *
from time import *
from prime import *
from factors import *


start = clock()

abundant = list(n for n in xrange(12,28124) if n < sum_of_factors(n))

sums = {}

for i in abundant:
	for j in abundant:
		if (i+j) > 28123:
			break
		else:
			sums[i+j] = 1

non_abun = [i for i in range(1,28124)]

print sum(non_abun) - sum(sums)

print clock() - start
