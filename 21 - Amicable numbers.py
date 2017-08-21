from math import *
from time import *
from prime import *
from factors import *

start = clock()

pair = dict((n, sum(factors(n))) for n in xrange(1, 10000))
print sum(n for n in xrange(1, 10000) if pair.get(pair[n], 0) == n and pair[n] != n)

print clock() - start