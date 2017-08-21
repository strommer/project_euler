from math import *
from time import *
from prime import *

count = 0
l = [int(x) for x in str(factorial(100))]

for x in l:
	count += x

print count