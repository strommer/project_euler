class x:
	pass
class y:
	pass
a = x()
print type(a)

print type(x)

b = y()
print isinstance(b,x)