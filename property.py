class TestClass:
	name = 'TEST'

	def __init__(self):
		print('TTTTTTTTTTTT')
	
	@property   # property는 멤버 변수로 @property 하면 함수가 변수로 변함
	def full_name(self):
		return self.name + ' ffffffffff'

test = TestClass()

print(test.full_name)  # 함수 호출 할 때 full_name() 함수가 full_name 변수로 호출 
# print(test.full_name()) # 에러 발생 변수를 함수로 호출 했기 때문에