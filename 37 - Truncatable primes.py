from math import *
from time import *
from prime import *
from factors import *
import re

start = clock()

sums = 0

for i in range(10,1000000):
	if isPrime(i):
		l = str(i)
		flag = 0
		for j in range(1,len(l)):
			if isPrime(int(l[j:])):
				if isPrime(int(l[:j])):
					flag += 1
		if (flag == len(l)-1):		
			sums += i

print sums

print clock() - start
