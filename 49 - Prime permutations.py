from math import *
from time import *
from prime_new import *
from prime import *
from permutations import *
from factors import *

start = clock()

num = get_primes(10000)

x = [i for i in num if i > 1000]

d = dict.fromkeys(["".join(sorted(str(i))) for i in x],())

for i in x:
	d["".join(sorted(str(i)))] += (i,) 

for k in d.keys():
	if len(d[k]) < 3:
		del d[k]

for v in d.values():
	for i in range(len(v)-2):
		for j in range(i+1,len(v)-1):
			for k in range(j+1,len(v)):
				if (v[k] - v[j] == v[j] - v[i]) and v[i] != 1487:
					print str(v[i])+str(v[j])+str(v[k])

print clock() - start
