a=7
b=5
c=a
a=b
b=c
print(a,b)

a=7
b=5
a,b=b,a
print(a,b)

a,b,c=7,5,3
a,b,c=c,b,a
print(a,b,c)