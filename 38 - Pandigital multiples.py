from math import *
from time import *
from prime import *
from factors import *
import re

start = clock()

sums  = 0
l = ''
large = "0"
for i in range(1,500000):
	j = 1
	m = ''
	while True:
		k = i*j
		l = m + str(k)
		if ("".join(sorted(l)) == '123456789' and j != 1):
			if (int(l) > int(large)):
				large = l
				print large
		elif (len(l) >= 10):
			break
		j += 1
		m = l


			
print clock() - start
