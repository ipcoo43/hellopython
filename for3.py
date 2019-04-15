s=0
for i in range(1,11):
	s+=i
print(s)

s=0
for i in range(1,11):
	if i%2==1:
		s+=i
print(s)

s=0
for i in range(1,11):
	if i%2==0:
		s+=i
print(s)

s=0
for i in range(1,11):
	s+=1/i
print(s)

s=0
for i in range(1,11):
	s+=i/(i+1)
print(s)