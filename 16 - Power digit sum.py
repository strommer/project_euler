from math import *
from time import *
from prime import *


x = str(2**1000)
sum = 0
for digit in x:
	sum = sum + int(digit)

print sum