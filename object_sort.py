class Student:
	def __init__(self,name,score):
		self.name=name
		self.score=score

	def __str__(self):
		return '{}:{}'.format(self.name, self.score)
	
students = [
	Student('홍일동',10),
	Student('홍삼동',30),
	Student('홍이동',20)
]

def print_students():
	print('-'*20)
	for s in students:
		print(s)

print_students()

students = sorted(students, key=lambda stu:stu.score)
print_students()

students.sort(key=lambda stu:stu.score)
print_students()

students.sort(key=lambda stu:stu.score, reverse=True)
print_students()

def sort_key(stu):
	return stu.score

students.sort(key=sort_key, reverse=True)
print_students()