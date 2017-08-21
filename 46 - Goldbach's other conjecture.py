from math import *
from time import *
from prime_new import *
from permutations import *

start = clock()

MAX =6000

primes = get_primes(MAX)
squares_2 = [2*i*i for i in range(1,MAX)]

nonprime = [i for i in range(1,MAX) if i not in primes and i%2 !=0]

nonprime_dict = dict.fromkeys(nonprime,0)

for i in primes:
	for j in squares_2:
		if(i+j) in nonprime_dict:
			nonprime_dict[i+j] = 1

for k in nonprime_dict:
	if nonprime_dict[k] == 0:
		print k


print clock() - start
