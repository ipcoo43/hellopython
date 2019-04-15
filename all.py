a=[False, True, False]
b=[False, False]
c=[True, True]
d=[1,2,3]
d.append(0)

print('all : {} =>'.format(a), all(a))
print('all : {} =>'.format(b), all(b))
print('all : {} =>'.format(c), all(c))
print('all : {} =>'.format(d), all(d))

print()
print('any : {} =>'.format(a), any(a))
print('any : {} =>'.format(b), any(b))
print('any : {} =>'.format(c), any(c))
print('any : {} =>'.format(d), any(d))