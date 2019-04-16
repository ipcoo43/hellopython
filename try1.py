s = '123'

try:
	print(int(s) + 1)
	print(int(s)/1)
except ValueError as e:
	print('ValueError occurs =>', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError occurs =>', e)
except IndexError as e:
	print('IndexError occurs =>', e)
except NameError as e:
	print('NameError occurs =>', e)
except TypeError as e:
	print('TypeError occurs =>', e)
except :
	print('Error occurs!!')
else:
	print('Success')
finally:
	print('Close')