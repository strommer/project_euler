from math import *
from time import *
from prime import *
from factors import *
import re

start = clock()

sums = 0

for x in range(3,100000):
	n = 0
	for digit in str(x):
		n += factorial(int(digit))
	if n == x:
		sums += x

print sums

print clock() - start
