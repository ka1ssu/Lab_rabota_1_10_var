import requests
from bs4 import BeautifulSoup as BS
r = requests.get("https://www.chitai-gorod.ru/search?phrase=python")
html = BS(r.content, 'html.parser')

name = []
price = []
for el in html.select(".products-list > .product-card.product"):
    title = el.select('.product-card__text > a')
    print(title[0].text)
    name.append(title[0].text)
    title2 = el.select('.product-card__price > .product-price > .product-price__value')
    # если убрать (> .product-price__value) то будет показываться старая и актуальная цена
    print(title2[0].text)
    price.append(title2[0].text)

with open("info.txt", 'w', encoding='utf-8') as file:
    for i in range(48):
        file.write(name[i] + price[i] + "\n")
