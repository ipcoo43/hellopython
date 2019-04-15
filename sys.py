import sys

print('sys.argv :',sys.argv, len(sys.argv))
sa=sys.argv

if len(sa)<2:
	sys.exit()

with open('sa[1]','r',encoding='utf-8') as fp:
	for line in fp:
		print(line)