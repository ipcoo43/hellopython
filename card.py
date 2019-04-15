import random

class Card:
	def __init__(self,m,n):
		self.m = m # 모양
		self.n = n # 숫자
cards = [
	Card('Clover',3),
	Card('Spade',9),
	Card('Heart',13)
]

random.shuffle(cards)
print(list(cards))