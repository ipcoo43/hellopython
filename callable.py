class Parent:
	name = 'Test'

	def get_name(self):
		print('qqqqqqq')
		return self.name
	
	def area(self,x,y):
		return x*y
	
	def static_method():
		print('STAIC')
	
class Child(Parent):
	def get_name(self):
		t = super().get_name()
		return 'Child Name:' + self.name
	
	def area(self,x,y):
		t = super().area(x,y)
		return t/2

parent = Parent()
child = Child()

print(child.get_name())

c=callable(parent.get_name)
print(c)

getattr(Parent,'static_method')()