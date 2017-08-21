from math import *
from time import *
from prime import *
from factors import *
import re

start = clock()

primes = []
for i in range (2,1000):
	if isPrime(i):
		primes.append(i)

print primes,len(primes)

maxcount, count, sum1,product = 0,0,0,0

for b in primes:
	for a in range(-999,1000,2):
		n,count = 0,0
		while True:
			sum1 = n*n + a*n +b
			if isPrime(sum1):
					count +=1
					n +=1
			else:
				if(count > maxcount):
					maxcount = count
					product = a*b
					print maxcount
				break
	
print product



print clock() - start
