a=int(input('a = '))
b=int(input('b = '))
c=int(input('c = '))

if b>a and b>c:
	a,b=b,a
if c>a and c>b:
	a,c=c,a
if b<c:
	b,c=c,b

print(a,'> ',b,'> ',c)
