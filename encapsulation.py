print('Encapsulation')

class Dog:
	def __init__(self, name):
		self.name = name     
		print(self.name,'메모리에 생성되었음')

	def speak(self):
		print(self.name,'멍멍하고 짖는다' )

	def wag(self):
		print(self.name,'꼬리를 흔든다')

	def __del__(self):   
		print(self.name,'메모리에서 정리됨')

class Puppy(Dog):  # Puppy는 Dog에 습성을 갖고 있는 틀
	def __init__(self):
		self.name = '포피가'
		self.color = 'Yello'
		print(self.name,'메모리에 생성됨')
	
	def speak(self):
		print(self.name,'Bow Wow라고 짖는다.')
	
	def __read_diary(self):   # 외부에서는 불러 낼 수 없지만
		print('Diary content!!!!!')
	
	def wag(self):
		self.__read_diary()    # 내부에서는 불러 낼 수 있음
		print(self.name,'꼬리를 흔든다')

# 마지막 자손의 메서드가 우선 순위가 높다
# 내가 불렀을 때 없으면 부모의 메소드를 찾아 간다.
# 내가 없으면서 부모도 없는 메소드를 불렀을 때는 에러가 발생 

dog = Dog('푸들이')
puppy = Puppy()

dog.speak()
puppy.speak()

dog.wag()
puppy.wag()

puppy.__read_diary()  # 에러 발생

print(dog.name,'|',puppy.name,'|',puppy.color)