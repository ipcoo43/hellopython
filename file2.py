def write_file():
	with open('a.csv','w',encoding='utf-8') as fp:
		fp.write('이름, 성별, 나이\n')
		fp.write('홍길동, 남, 14\n')
		fp.write('홍이동, 남, 15\n')

def append_file():
	with open('a.csv','a',encoding='utf-8') as fp:
		fp.write('홍삼동, 남, 16')

def read_file():
	with open('a.csv','r',encoding='utf-8') as fp:
		for line in fp:
			print('line>> ', line)

write_file()
append_file()
read_file()