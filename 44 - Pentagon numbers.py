from math import *
from time import *
from prime import *
from permutations import *

start = clock()


pent = []

for i in range(4000):
	pent.append(i*(3*i-1)/2) 

pentdict = dict.fromkeys(pent)

flag = 0
low = 1000000000


for j in xrange(1,len(pent)/2):
	for k in xrange(j+1,len(pent)):
		if pentdict.has_key(pent[k]-pent[j]) and pentdict.has_key(pent[j]+pent[k]):
				low = pent[k]-pent[j]		
				print j,"-",k,"=",low

print low
			

print clock() - start
