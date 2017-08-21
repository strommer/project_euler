from math import *
from time import *
from prime import *
from permutations import *

start = clock()

x = map(chr, range(65,91))

score = {}

for i in range(0,26):
	score[x[i]] = i +1

words = (open('words.txt','r').readline()).split(',') 

array = [i*(i+1)/2 for i in range(30)]

triangle = []

for i in range(len(words)):
	words[i] = words[i].strip('"')
	sum1 = 0
	for x in words[i]:
		sum1 += score[x]
	if sum1 in array:
		triangle.append(sum1)

print len(triangle)
	


print clock() - start
