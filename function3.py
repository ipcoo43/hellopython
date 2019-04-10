print('두 수를 입력 받아 사칙 연산 수행 함수')
print('input a OP b => result')
print('> 3 + b')

def plus(a,b):
	return a+b

def minus(a,b):
	return a-b

def mul(a,b):
	return a*b

def div(a,b):
	if b == 0:
		return a
	return a/b

cmd = input('수식을 입력하세요(usage: 2+3) > ')
cmds = cmd.split(' ')

# QQQ  : 배포 하기 전에 확인 
# @ToDo : 해야 할 일 
# @Try  : 연습 할 곳

a, op, b = cmds
# print(a,op,b)
a, b = int(a), int(b)

# a,op,b = int(cmds[0]), cmds[1], int(cmds[2])
if op == '+':
	r = plus(a,b)
elif op == '-':
	r = minus(a,b)
elif op == '*':
	r = mul(a,b)
else:
	r = div(a,b)

if op == '/':
	print('{} {} {} = {:.2f}'.format(a,op,b,r))
else:
	print('{} {} {} = {:d}'.format(a,op,b,r))