from math import *
from time import *
from prime import *
from factors import *
import re

start = clock()

sums = 0

for i in range(1000000):
	if (str(i) == str(i)[::-1]):
		if(str(bin(i)[2:]) == str(bin(i)[2:])[::-1]):
			sums += i

print sums

print clock() - start
