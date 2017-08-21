from math import *
from time import *
from prime import *
from factors import *
import re

start = clock()
sum = 0

for i in range(1,1001):
	sum += i**i

print str(sum)[-10:]
print clock() - start
