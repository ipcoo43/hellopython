text=input('단어 한나 입력 : ')
li=list(text)

for i in li:
	print("'{}'".format(i),end=',')


a=input('정수 하나 입력 : ')
li=list(a)
for i in range(len(li)):
	li[i]=int(li[i])
	print('[{}]'.format(li[i]*(10**((len(li)-1)-i))))

# print(li[0]*(10**4))
# print(li[1]*(10**3))
# print(li[2]*(10**2))
# print(li[3]*(10**1))
# print(li[4]*(10**0))
