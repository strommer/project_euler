from math import *
from time import *
from prime import *
from factors import *
from collections import defaultdict
import re
from isPSquare import *

start = clock()

large = defaultdict(list)

for i in range(1,1000):
	for j in range(1,1000):
		if isPSquare(i*i +j*j):
			k = int(sqrt(i*i +j*j))
			p = i+j+k
			if (p <= 1000):
				large[p].append([i,j,k])

maxim = 0
for i in large:
	if(len(large[i])> maxim):
		maxim = len(large[i])
		val = i

print val
print clock() - start
