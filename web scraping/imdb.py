from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")
temp_rows = soup.find("tbody",attrs={"class":"lister-list"})
rows = temp_rows.findAll("tr")

titles = []
ratings = []
years = []

for row in rows:

    title = row.find("td",attrs={"class":"titleColumn"})
    rating = row.find("td",attrs={"class":"ratingColumn imdbRating"})
    t = (title.text).split()
    new_string = " "

    for i in range(1,len(t)):
        new_string += t[i] + " "

    titles.append(new_string)
    ratings.append(rating.text.strip())

for title in titles:
    for s in range(len(title)):
        if title[s]=='(':
            years.append(title[s+1:s+5])

movies_csv = pd.DataFrame({'Title':titles,'Year':years,"Rating":ratings})
movies_csv.to_csv('movies.csv', index=False, encoding='utf-8')

