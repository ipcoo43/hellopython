for n in range(1,101):
	c = str(n).count('3') + str(n).count('6') + str(n).count('9')
	if c==0:
		print(n)
	else:
		print('짝'*c)
