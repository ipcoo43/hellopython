a=[1,2,3]
b=[4,5,6]
c=[7,8]

print('a={},b={},c={}'.format(a,b,c))
print('list(zip(a,b))')
print('a={},b={},c={}'.format(a,b,list(zip(a,b))))
print('list(zip(a,c))')
print('a={},c={},r={}'.format(a,c,list(zip(a,c))))

