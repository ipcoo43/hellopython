import random

print(random.randrange(1,7))
print(random.randint(1,6))

lst=[1,2,3,4,5,6]
random.shuffle(lst)
print(lst)

lst=list(range(1,14))
random.shuffle(lst)
print(lst)
