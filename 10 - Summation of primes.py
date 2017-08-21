from math import *
from time import *
from prime import *

sum = 0

for x in xrange(2,2000000):
	if isPrime(x):
		sum = sum +x

print sum