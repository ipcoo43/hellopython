print('Static(정적) Method on class')
print('Non self argument')

class Dog:
	def m1(self):
		print('m1')
	
	def m2():  # self가 없으면 정적 메소드가 됨, 인스턴스 만들 필요 없음
		print('m2')

class Calc:
	def plus(a,b):
		return a+b
		 
dog = Dog()
dog.m1()
Dog.m2()