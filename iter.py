a=[1,2,3]
it=iter(a)
print('iter : {} => '.format(a), it)
print('list가 iter이 되면 next()사용')
print('메모리에 올라와있는 iter에 있는 값을 next()를 통하여 사용하고')
for i in a:
	print('next(it) =>',next(it,None))
print('iter에는 모두 메모리에서 지워짐 list(it) => ',list(it))