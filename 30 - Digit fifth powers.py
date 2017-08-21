from math import *
from time import *
from prime import *
from factors import *
import re

start = clock()
sum1 = 0
main_sum = 0

for i in range(2,1000000):
	sum1 =0
	for digit in str(i):
		sum1 += int(digit)**5
	if sum1 == i:
		main_sum += sum1
		print i

print main_sum

print clock() - start
