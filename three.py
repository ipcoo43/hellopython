today = input('날짜 입력 : ')
li=today.split('.')

li[0]=int(li[0])
li[1]=int(li[2])
li[2]=int(li[3])

print('%d.%d.%d'%(li[0],li[1],li[2]))
print('%04d.%02d.%02d'%(li[0],li[1],li[2]))

print(li[0]+'.'+li[1].zfill(2)+'.'+li[2].zfill(2))

print('{}.{}.{}'.format(li[0],li[1].zfill(2),li[2].zfill(2)))

jumin=input('주민번호 입력 : ')
li=jumin.split('-')
print(li[0]+li[1])
print(li[0],end='')
print(li[0])


silsu=input('실수 입력 : ')
li=silsu.split('.')
print(li[0])
print(li[1])

silsu2=float(input('실수 입력 : '))
print(int(silsu2))
print(silus2-int(silsu2))