from math import *
from time import *
from prime import *
from factors import *
import re

start = clock()

cir_primes = []

def shift(seq, n):
    n = n % len(seq)
    return "".join(seq[n:]+seq[:n])

for i in range(2,1000000):
	if isPrime(i):
		temp = [k for k in str(i)]
		for j in range(len(temp)):
			if not isPrime(int(shift(temp,j))):
				break
		else:
			cir_primes.append(i)

print len(cir_primes)


print clock() - start
