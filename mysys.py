import os

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

# os.system('cls' if os.name == 'nt' else 'clear')

