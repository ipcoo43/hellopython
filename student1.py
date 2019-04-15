from functools import reduce
from Student import Student

students=[]
with open('students.csv','r',encoding='utf-8') as fp:
	for i,line in enumerate(fp):
		if i==0: continue
		students.append(Student(line))

students.sort(key=lambda stu:stu.score, reverse=True)

m=list(map(lambda stu:stu.make_grade(),students))

# A if type(x)==int else B
# 이항연산 => type(x)==int ? A : B
# if type(x)==int":
#	print(A)
# else:
#	print(B)

# def sumfn(x,y):
#	if type(x)==int:
#		return x+y.score
#	else:
#		return x.score+y.score
# total = reduce(sumfn,students)

total = reduce(lambda x,y:(x if type(x)==int else x.score)+y.score,students)
avg = total/len(students)
print('총점, 평균 >>>',total, total/avg)
print('이름\t성별\t나이\t학점')
print('----\t----\t----\t----')
for s in students:
	print(s)

print('-'*5,'평균 {} 보다 큰 점수'.format(avg),'-'*5)
for s in students:
	if s.score >= avg:
		print(s.name, s.score)