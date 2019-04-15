import datetime

now=datetime.datetime.now()
lst=['now', 'now.year','now.month', 'now.day', 'now.hour', 'now.minute', 'now.second']
for i in lst:
	print('{} :'.format(i), eval(i))

print("now.strftime('%Y-%m-%d %H:%M:%S') :",now.strftime('%Y-%m-%d %H:%M:%S'))
print(now.strftime('%Y{} %m{} %d{} %H{} %M{}'.format(*"년월일시분")))

print(now + datetime.timedelta(weeks=1))

print(now.replace(year=(now.year+1)))