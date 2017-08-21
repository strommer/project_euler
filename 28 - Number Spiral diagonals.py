from math import *
from time import *
from prime import *
from factors import *
import re

start = clock()
sum1 = 0

for i in range(3,1002,2):
	j = i-1;
	sum1 = sum1 + i*i + i*i-j + i*i-2*j+ i*i - 3*j
print sum1+1;
print clock() - start
