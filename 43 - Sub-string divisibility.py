from math import *
from time import *
from prime import *
from permutations import *

start = clock()

sums = 0
primes = [nthPrime(i) for i in range(1,8)]
flag = 0

for perm in permutations('0123456789'):
	flag = 0
	for i,p in enumerate(primes):
		if (int(perm[(i+1):(i+4)])%p == 0):
			flag+= 1
	if flag == 7:
		sums += int(perm)
		print sums

print sums


print clock() - start
