from bs4 import BeautifulSoup
import requests

url = 'https://play.google.com/store/apps/category/GAME/collection/topselling_paid'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
# print(res.text)

card_list = soup.select('div.card-list')
# print(card_list)  # __str__(toString)을 해 줌
print('A>>>',len(card_list),card_list[0].get('class'))
for i in card_list:
	cards = i.select('.card')
	print('cards len>>',len(cards))
	for c in cards:
		title = c.select('a.title')[0].text.strip()
		# comp = c.select('a.subtitle')[0].text
		comp = c.select('a.subtitle')[0].get('title')
		print('B>>>',c.get('class'), [title, comp])