print('두 수를 입력 받아서 사칙연산을 수행하는 함수')

def plus(a,b):
	return a+b

def minus(a,b):
	return a-b

def multi(a,b):
	return a*b

def divid(a,b):
	return a/b

cmd = input('두 수 입력 해 수세요 예시) 3,5 => ')
cmds = cmd.split(',')
a,b=int(cmds[0]),int(cmds[1])

if a < b :
	a, b = b, a

print('{} + {} ='.format(a,b), plus(a,b))
print('{} - {} ='.format(a,b), minus(a,b))
print('{} * {} ='.format(a,b), multi(a,b))
print('{} / {} ='.format(a,b), divid(a,b))

