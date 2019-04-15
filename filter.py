a=range(-5,6)
print('a={}'.format(list(a)))
print('a에서 음수만 filter 하기')
print('list(filter(lambda x:x<0,a)) = ',list(filter(lambda x:x<0,a)))

def fn(x):
	return x<0
print(list(filter(fn,a))) 
print(list(filter(lambda x:x>0,a)))
print(list(filter(lambda x:x%2==0,a)))