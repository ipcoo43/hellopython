a=(1,2,3,4)

def fn(n):
	return n*2
print(list(map(fn,a)))

print(list(map(lambda x:x*3,a)))