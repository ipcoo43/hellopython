print('Function(Class에 존재하면 Method로 부름)')

def fn():  # 함수 선언
	print('fn called')

fn()  # 함수 호출 할 때 메모리에 로딩

def exp(x):
	return x**2

print(exp(3))
print(exp(9))

def get_fruits():
	return ['orange','apple','banner']

print(get_fruits())
print(get_fruits()[1])


def get_name():
	return 'kent', 'Beck'

def full_name(first_name, last_name):
	return first_name + ' ' + last_name

name = get_name()
print(name, full_name('AAA','BBB'))

def var_param(a, *vp):  # *가 붙으면 가변적이 파라미터 
	print(type(vp))     # tuple로 들어감
	print(a, len(vp), vp[len(vp)-1])

var_param(1,2,3,4)

def default_param(a, vp=100):  # vp에 초기값 부여
	print(a, vp)

default_param(1)