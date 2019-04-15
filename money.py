li=[50000,10000,5000,1000,500,100,50,10,5,1]
n=int(input('number = '))
for i in li:
	m=n//i
	n=n%i
	print(i, ' => ', m)