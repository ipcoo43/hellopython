class Test:
	name = 'test'

test = Test()
test2 = Test()
test3 = test
print('------ test ------')
print('hash =',hash(test),hex(hash(test)))
print('id =',id(test),hex(id(test)))

print('------ test2 ------')
print('hash =',hash(test2),hex(hash(test2)))
print('id =',id(test2),hex(id(test2)))

print('------ test3 = test ------')
print('hash =',hash(test3),hex(hash(test3)))
print('id =',id(test3),hex(id(test3)))
print()
