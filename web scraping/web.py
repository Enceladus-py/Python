from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

driver = webdriver.Chrome("chromedriver")

page_number = 1
names = []
prices = []
ranks = []
comments = []

while(page_number<20):

    driver.get("https://www.vatanbilgisayar.com/notebook/?page={}".format(page_number))
    content = driver.page_source
    soup = BeautifulSoup(content,features="html.parser")

    laptops = soup.findAll("div",attrs={"class":"product-list product-list--list-page"})

    for laptop in laptops:

        name = laptop.find("div",attrs={"class":"product-list__product-name"})
        price = laptop.find("span",attrs={"class":"product-list__price"})
        cprice = laptop.find("span",attrs={"class":"product-list__current-price"})
        star = laptop.find("span",attrs={"class":"score"})
        cmt = laptop.find("a",attrs={"class":"comment-count"})

        names.append(name.text)
        comments.append('\n' + cmt.text + '\n')

        if '0%' == str(star)[33:35]:
            ranks.append('\n0\n')
        else:
            ranks.append('\n' + str(star)[33:35] + '\n')

        if cprice.text:
            prices.append('\n' + price.text + "\n" + strike(cprice.text) + '\n')
        else:
            prices.append('\n' + price.text + '\n')

    page_number += 1

products = pd.DataFrame({'Price (TL)':prices,'Product Name':names,"Ranking":ranks,"Comment Count":comments})
products.to_csv('products.csv', index=False, encoding='utf-8')