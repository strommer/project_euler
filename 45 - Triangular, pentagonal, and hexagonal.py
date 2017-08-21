from math import *
from time import *
from prime import *
from permutations import *

start = clock()

triangle = []
pentagonal = []
hexagonal = []

for i in range(1,100000):
	triangle.append(i*(i+1)/2) 
	pentagonal.append(i*(3*i-1)/2) 
	hexagonal.append(i*(2*i-1)) 

pentagonaldict = dict.fromkeys(pentagonal)
hexagonaldict = dict.fromkeys(hexagonal)

for j in triangle:
	if pentagonaldict.has_key(j) and hexagonaldict.has_key(j):
		print triangle.index(j)+1,'-->',j

print clock() - start
