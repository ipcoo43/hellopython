from bs4 import BeautifulSoup
import requests

url = 'https://play.google.com/store/apps/category/GAME/collection/topselling_paid'
res = requests.get(url)

# 생성자
# parser : html, json
# html를 파싱 한 후에 soup에 담음
soup = BeautifulSoup(res.text,'html.parser')

# soup.select('div.card-list')에 크롬 콘솔에서 찾은 $('div.card-list')
# card_list에는 card-list 태그가 들어 있음
# card-list는 태그(다른 곳에서는 Element)를 가져 옴
card_list = soup.select('div.card-list')
# get하면 attribute(class, style, id)를 가져 옴 
# card_list.get('class')는 div 태그 안에 attribute의 class를 가져 오겠다고 함
print('A >>>', card_list.get('class'))
# card_list안에 n개의 안에서 .card를 찾아와라
for i in card_list:
	cards = i.select('.card')
	for c in cards:
		print('B >>>',c.get('class'))


# card_list[0].sleelct('.card')