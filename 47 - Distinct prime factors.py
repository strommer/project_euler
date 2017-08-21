from math import *
from time import *
from prime_new import *
from permutations import *
from factors import *

start = clock()

MAX = 150000
count = 0

for i in range(MAX):
	for j in range(i,i+4):
		if len(prime_factors(j)) == 4:
			count += 1
			if count == 4:
				print i
		else:
			break
	count = 0


print clock() - start
