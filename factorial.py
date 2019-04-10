print('Recursive Function : 재귀 함수')
print('자신의 로직을 내가 불러야 한다')

def factorial(n):  # 4! = 4*3*2*1
	if n == 1:
		return 1
	else:
		return n*factorial(n-1) # 4 * 3! 이면 4 * 3*2*1 로 리턴됨

print(factorial(4))