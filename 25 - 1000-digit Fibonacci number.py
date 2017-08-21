from math import *
from time import *
from prime import *
from factors import *


start = clock()

a = 1 
b = 1

count = 2
flag = 0

while True:
	fib = a + b
	a = b
	b = fib
	count +=1

	if fib/10**1000 > 1:
		print count
		break

print clock() - start
