from math import *
from time import *
from prime import *
from factors import *
import re

start = clock()
sum1 = 0

num = {}

for a in range(2,101):
	for b in range(2,101):
		num[a**b]  = 1

print len(num)

print clock() - start
