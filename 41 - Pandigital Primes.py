from math import *
from time import *
from prime import *
from permutations import *

start = clock()

large = 0
x = ''

for i in range(1,8):
	x += '%d' %i
	for perm in permutations(x):
		if(isPrime(int(perm))):
			large = perm

print large

print clock() - start
