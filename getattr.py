class TestClass:
	name = 'Test'

	def get_name(self):
		print('qqqqqqq')
		return self.name
	
	def area(self,x,y):
		return x*y
	
	def static_method():
		print('STAIC')
	
class Child(TestClass):
	def get_name(self):
		t = super().get_name()
		return 'Child Name:' + self.name
	
	def area(self,x,y):
		t = super().area(x,y)
		return t/2

test = TestClass()
child = Child()

print(hasattr(test,'get_name'))
print(getattr(test,'get_name')())

# cmd = input('Input the function name >> ')
# getattr(test, cmd)()



