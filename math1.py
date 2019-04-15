import math

lst = ['math.sqrt(9)','math.sin(1)','math.cos(1)','math.tan(1)','math.floor(2.5)','math.ceil(2.5)','math.log(2)']

for i in lst:
	print("{} :".format(i), eval(i))


lstA=[1.2, 2.4, 3.6]
print('lstA =',lstA)
print('sum(lstA) = {} :',sum(lstA))
print('math.fsum(lstA) = {} :',math.fsum(lstA))

print('math.pi =',math.pi)
print('pow(2,3) =',pow(2,3))
print('math.pow(2,3) =',math.pow(2,3))

print(dir(math))