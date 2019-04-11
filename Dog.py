print('Dog Class')

# __(2개) 시스템  함수
# _(1개) 나만의 함수
# self : 내 자신 (진짜 나), Dog() 클래스가 아닌 puddle의 인스턴스가 self이다. 
class Dog:
	                            # __init__는 시작 할 때 작업, connect
	def __init__(self, name):   # Dog() 호출하는 순간 __init__가 가장 먼저 호출 됨
		                        # constructor(생성자) : 생성될 때 반드시 실행 해야 할 함수
		self.name = name        # 생겨난 공간 이름을 Dog라고 지어 버림
		print(self.name,'가(이) 메모리에 생성되었음')
    # self는 내가 만들어질 때의 인스턴스, 인스턴스 자신
	def speak(self):
		print(self.name,'는(은) 멍멍하고 짖는다' )

	def wag(self):
		print(self.name,'가(이) 꼬리를 흔든다')

	def __del__(self):    # 메모리에서 해제 될 때 호출 됨, 정리 작업, close
		print(self.name,'가(이) 메모리에서 정리됨')

puddle = Dog('푸들')  # 메모리에 puddle라는 공간 생성, 푸들의 이름은 푸들
sheperd = Dog('세퍼드') # 메모리에 shepred라는 공간 생성, 세퍼드의 이름은 세퍼드

puddle.speak() 
sheperd.speak()