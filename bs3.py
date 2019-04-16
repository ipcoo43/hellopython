print('''
<pre>
문제1) 플레이스토어 유료 게임 랭킨 60위 까지 게임의,
 - 게임명
 - 제조사
 - 평점
 - 가격
 - 대표 아이콘 이미지 경로
를 스크래핑해서 csv 파일로 저장하시오

문제2) 각 게임의 상세 페이지로 이동하여 출시일, 출시일등 기타정보 수집
</pre>	
''')

from bs4 import BeautifulSoup
import requests
from Game import Game

url = 'https://play.google.com/store/apps/category/GAME/collection/topselling_paid'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
card_list = soup.select('div.card-list')

print('A>>>', type(card_list), type(card_list[0]))
games = []
for i in card_list:
	cards = i.select('div.card')
	print('B>>>', len(cards))
	for c in cards:
		games.append(Game(c))

for i in games:
	print(i)
