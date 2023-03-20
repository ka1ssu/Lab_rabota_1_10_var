def parser():
    import requests
    import xlsxwriter
    from bs4 import BeautifulSoup as BS
    r = requests.get("https://www.chitai-gorod.ru/search?phrase=python")
    html = BS(r.content, 'html.parser')
    name = []
    author = []
    price = []
    col = 1
    counter = 0
    for el in html.select(".products-list > .product-card.product"):
        title1 = el.select('.product-title > .product-title__head')
        name.append(title1[0].text)
        title2 = el.select('.product-title > .product-title__author')
        author.append(title2[0].text)
        title3 = el.select('.product-card__price > .product-price > .product-price__value')
        price.append(title3[0].text)
        print(title1[0].text, title2[0].text, title3[0].text)
        counter += 1

    workbook = xlsxwriter.Workbook('ResultsPARSER.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'Название')
    worksheet.write(0, 1, 'Автор')
    worksheet.write(0, 2, 'Цена')
    for i in range(counter):
        worksheet.write(col, 0, name[i])
        worksheet.write(col, 1, author[i])
        worksheet.write(col, 2, price[i])
        i += 1
        col += 1
    workbook.close()