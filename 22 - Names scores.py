from math import *
from time import *
from prime import *
from factors import *


start = clock()

x = map(chr, range(65,91))

score = {}

for i in range(0,26):
	score[x[i]] = i +1

names = (open('names.txt','r').readline()).split(',')

names.sort()

for i in range(len(names)):
	names[i] = names[i].strip('"')
	sum1 = 0
	for x in names[i]:
		sum1 += score[x]
	names[i] = sum1*(i+1)


print sum(names)

print clock() - start