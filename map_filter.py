a=range(-5,6)

print('lambda x:x<0,a')
print('filter =',list(filter(lambda x:x<0,a)))
print('map =',list(map(lambda x:x<0,a)))
print()
print('lambda x:x*2,a')
print('filter =',list(filter(lambda x:x*2,a)))
print('map =',list(map(lambda x:x*2,a)))