from math import *
from time import *
from prime import *


year = (31,28,31,30,31,30,31,31,30,31,30,31)

st = 1
count = 0

for x in range(1901,2000):
	for month in year:
		if ((x%4 == 0 or x == 2000) and (month == 28)):
			month = 29
		st += month
		if(st%7 == 0):
			count += 1

print count