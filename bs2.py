from bs4 import BeautifulSoup4
import requests

url = 'https://play.google.com/store/apps/category/GAME/collection/topselling_paid'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
print(res.text)
exit()
card_list = soup.select('div.card-list')
print('A>>>',card_list.get('class'))

for i in card_list:
	cards = i.select('.card')
	for c in cards:
		print('B>>>',c.get('class'))