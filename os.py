import os

li=['os.name','os.getcwd()','os.chdir(".")','os.getcwd()','os.system("ls")','os.system("python a.py")']
for i in li:
	print('{} :'.format(i), eval(i))