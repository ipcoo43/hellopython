from functools import reduce

product = 1
lst = [1,2,3,4]
for num in lst:
	product = product * num
	print(product,end=',')
print('product1 >>',product)

print('product2 >>',reduce(lambda x,y:x*y,lst))