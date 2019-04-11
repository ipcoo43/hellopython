print('Class & Object & Instance')
print('CamelCase vs Pascalcase vs snake_case')
print('세상의 모든 물건은 object이다')
print('Class = 붕어빵(object) + 틀 (무엇을 만들어 내는 기계)')
print('Instance : 만들어낸 붕어빵 (살아있는 것, 내가 먹을 수 있는 것)')
print('isinstance(instanceX,Class) : instanceX가 Class로 만들어 졌는냐?')
print('모든 object는 method:행동, property:상태값 을 갖고 있음')
print('객체 지향 프로그램(Object-Oriented Programming, OOP)')
print('OOP 특징:추상적,감출수있다,상속,다양성 ')
print('Class has properties and methods')

class Dog:  # Dog는 개의 속성을 갖고 있음, 습성을 갖고 있음
	def __init__(self):
		self.name = 'Dog'  # 내 이름은 dog라는 (상태) 값을 가짐
		print('Dog was Born')
	def speak(self):       # 짖을 수도 있고 ( 행동 )
		print('Yelp!', self.name)
	def wag(self):         # 꼬리도 흔든다 ( 행동 )
		print("Dog's wag tail")
	def __del__(self):
		print('destory!!')

s = Dog()
p = Dog()

class Bank:   # 은행의 습성을 갖고 있음, 
	def __init__(self):
		self.money = 0   # money을 0으로 초기화 시킨 상태, money는 Bank의 멤버 변수
		                 # self 자기 자신
		print('Bank가 생성되었습니다.')

	def deposit(self, money): # deposit(입급)이라는 행동을 갖음, 함수는 행동(동작)
		self.money += money

woori = Bank()
shinhan = Bank()