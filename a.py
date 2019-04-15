class TestClass:
	name = 'TEST'

	def get_name(self):
		print('qqqqqqqq')
		return self.name

class Child(TestClass):
	def get_name(self):
		super().get_name()
		return 'Chile Name ' + self.name


test = TestClass()
child = Child()
print('1111>>', child.get_name())

c = callable(test.get_name)
print('cccc> ',c)