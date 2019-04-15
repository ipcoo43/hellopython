a=int(input('a = '))
b=int(input('b = '))

if a>b:
	print(a)
else:
	print(b)

a=int(input('a = '))
b=int(input('b = '))
c=int(input('c = '))

if a>b and a>c:
	print(a)
elif b>a and b>c:
	print(b)
else:
	print(c)

max1=0
for i in range(5):
	a = int(input('number ='))
	if max1<a:
		max1=a
print(max1)

min1=100
for i in range(5):
	a = int(input('number = '))
	if min1>a:
		min1=a
print(min1)