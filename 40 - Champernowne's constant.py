from math import *
from time import *
from prime import *
from factors import *
from collections import defaultdict
import re
from isPSquare import *

start = clock()

d = ''

for i in range(1,1000001):
	x = '%d' %i
	d += x


print int(d[0])*int(d[9])*int(d[99])*int(d[999])*int(d[9999])*int(d[99999])*int(d[999999])

print clock() - start
