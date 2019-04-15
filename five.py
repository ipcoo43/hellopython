print('10진수 정수 -> 2,8,16 문자열 / 함수 사용')
print(bin(5))
print(oct(15))
print(hex(15))

print('10진수 정수 -> 2,8,16 문자열 / format')
print('{:#b}'.format(5))
print('{:#o}'.format(15))
print('{:#x}'.format(15))

print('2,8,16 정수 -> 10진수 정수')
print('0b101')
print('0o17')
print('0xf')

print('2,8,16 문자열 -> 10진수 정수')
print(int('101',2))
print(int('17',8))
print(int('f',16))

a=int(input('10->8 : '))
print(oct(a))
print('{:#o}'.format(a))

b=int(input('10->16 : '))
print(hex(b))
print('{:#x}'.format(b))

c=int(input('8->16 : '),8)
print(c)

d=int(input('16->8'),16)
print(oct(d))
print('{:#o}'.format(d))