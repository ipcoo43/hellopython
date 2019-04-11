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

def input_calc():
	cmd = input('수식을 입력하세요(usage: 2 + 3) => ')
	cmds = cmd.split(' ')
	a,op,b = cmds
	a,b = int(a), int(b)

	if op == '+':
		r = plus(a,b)
	elif op == '-':
		r = minus(a,b)
	elif op == '*':
		r = mul(a,b)
	else:
		r = div(a,b)

	if op == '/':
		print('Answer is {:.2f}'.format(r))
	else:
		print('Answer is {:d}'.format(r))

while(True):
	input_calc()