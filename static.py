class TestClass:
	name = 'TEST'

	def __init__(self):
		print('Memory Create')
	
	@staticmethod
	def static_method():
		print('STATIC')

test = TestClass()

test.static_method()
TestClass.static_method()