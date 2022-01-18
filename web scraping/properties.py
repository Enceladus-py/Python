from numpy import VisibleDeprecationWarning
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def arr_to_str(arr):
    for s in range(len(arr)):
        st = ", ".join(arr[s])
        arr[s] = st

driver = webdriver.Chrome("chromedriver")

names = []
types = []
locations = []
readies = []
distances = []
general_features = []
technical_features = []
sport = []
view = []
top = []
security = []
prices = []
descriptions = []
length = 0

driver.get("https://www.tremglobal.com/properties")
content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")
props = soup.findAll("div",attrs={"class":"col-xl-4 col-md-6 col-12 property-pad d-none"})

for prop in props:
    name = prop.find("h4",attrs={"class":"ps-title"})
    names.append(name.text.strip())
    link = prop.find("a").get("href")
    driver.get(link) 
    content = driver.page_source
    soup = BeautifulSoup(content,features="html.parser")
    details = soup.find("div",attrs={"class":"attributes-content"})
    iterator = details.find("div",attrs={"class":"attributes-text"})
    location = iterator.findNext("span")
    locations.append(location.text.strip())
    iterator = iterator.findNext("span")
    project_type = iterator.findNext("span")
    types.append(project_type.text.strip())
    iterator = iterator.findNext("span")
    ready = iterator.findNext("span")
    readies.append(ready.text.strip())
    iterator = iterator.findNext("span")
    distance =  iterator.findNext("span")
    distances.append(distance.text.strip())
    table = soup.find("div",attrs={"class":"table-responsive"})
    table_children = table.findChildren("table")

    prices.append([])
    for child in table_children[1:]:
        row = child.find("tr")
        td = row.findChildren("td")
        td[0] = td[0].text.strip()            
        td[1] = td[1].text.strip()            
        td[2] = td[2].text.strip()            
        st = td[0] + ": " + td[1] + ", " + td[2] + "; "
        prices[length].append(st)

    general_features.append([])
    technical_features.append([])
    security.append([])
    sport.append([])
    view.append([])
    top.append([])

    ftrs = soup.find("ul",attrs={"class":"features-list"}) 
    if ftrs == None:
        general_features[length].append("None")
        technical_features[length].append("None")
        security[length].append("None")
        top[length].append("None")
        sport[length].append("None")
        view[length].append("None")
    else:
        children = ftrs.findChildren("li")
        for child in children[1:]:
            general_features[length].append(child.text.strip())

        ftrs = ftrs.findNext("ul")
        children = ftrs.findChildren("li")
        for child in children[1:]:
            technical_features[length].append(child.text.strip())
        
        ftrs = ftrs.findNext("ul")
        children = ftrs.findChildren("li")
        for child in children[1:]:
            security[length].append(child.text.strip())

        ftrs = ftrs.findNext("ul")
        children = ftrs.findChildren("li")
        for child in children[1:]:
            top[length].append(child.text.strip())

        ftrs = ftrs.findNext("ul")
        children = ftrs.findChildren("li")
        for child in children[1:]:
            sport[length].append(child.text.strip())

        ftrs = ftrs.findNext("ul")
        children = ftrs.findChildren("li")
        for child in children[1:]:
            view[length].append(child.text.strip())

    print(length)
    length += 1
    desc = soup.find("div",attrs={"class":"why-this-property"}) 
    if desc != None:
        descriptions.append(desc.text.strip())
    else:
        descriptions.append("None")

arr_to_str(general_features)
arr_to_str(technical_features)
arr_to_str(security)
arr_to_str(sport)
arr_to_str(top)
arr_to_str(view)
arr_to_str(prices)

products = pd.DataFrame({'Property Name':names, "Location":locations, "Ready By":readies, "Project Type":types, 
"Distance to Airport":distances, "General Features":general_features, "Technical Features":technical_features,
"Security Specifications":security, "Sport Activities": sport, "Top Features": top, "Project View": view,
"Project Rooms":prices, "Description":descriptions })
products.to_excel('properties.xlsx', index=False, encoding='utf-16')