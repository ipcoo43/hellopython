from bs4 import BeautifulSoup
import requests
#from Game import Game
from jputils.Game import Game

url = 'https://play.google.com/store/apps/category/GAME/collection/topselling_paid'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
card_list = soup.select('div.card-list')

isTest = False   # QQQ : 배포시 False로 할 것
print('A>>>', type(card_list), type(card_list[0]))
games = []
for i in card_list:
	cards = i.select('div.card')
	print('B>>>', len(cards))
	tmpi = 0
	for c in cards:
		if isTest:
			tmpi += 1
			if tmpi>10: break;
		games.append(Game(c))
# QQQ
for i in games:
	print(i)

with open('games.csv','w',encoding='utf-8') as fp:
	for i in games:
		fp.write('게임명\t제조사\t가격\평점')
		fp.write(i.to_str() + '\n')