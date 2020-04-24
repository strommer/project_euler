def permutations(val):
	res = []
	if len(val) == 1:
		res = [val]
	else:
		for i, c in enumerate(val):
			for perm in permutations(val[:i]+val[i+1:]):
				res += [c+perm]
				print res

	return res

def permutations_gen(string):
    if not string:
        yield ''
    for i, d in enumerate(string):
        for perm in permutations_gen(string[:i] + string[i+1:]):
            yield d + perm
