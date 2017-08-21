from math import *
from time import *
from prime import *
from factors import *
import re

start = clock()

string = '123456789'
x = sorted(string)

sums = {}

for a in range(1000):
	if '0' not in str(a):
		for b in range(10000):
			if '0' not in str(b):
				if (sorted(str(a)+str(b)+str(a*b)) == x):
					sums[a*b] = 1

print sum(sums)

print clock() - start
