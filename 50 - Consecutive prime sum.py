from math import *
from time import *
from prime_new import *
from prime import *
from permutations import *
from factors import *

start = clock()
maxi = 1000000
primes = get_primes(maxi)

kmax = 1

for i in range(len(primes)):
	k=kmax
	while (k <= len(primes)-i):
		z = sum(primes[i:i+k])
		if z > maxi:
			break
		if isPrime(z):
			if k >= kmax:
				kmax = k
				zmax = z
		k += 1

print zmax

print clock() - start
