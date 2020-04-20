import requests
from bs4 import BeautifulSoup

req = requests.get("https://search.shopping.naver.com/search/category.nhn?pagingIndex=1&pagingSize=40&viewType=list&sort=review&cat_id=50000938")
if req.status_code != 200 :
    print("failed", req.status_code)

html = req.text
bs = BeautifulSoup(html, "html.parser")

box = bs.find_all("div", class_="info")

title = []
price = []

for b in box :
    title.append(b.find("div", class_="tit").find("a", class_="link").text)
    if b.find("span", class_="price").find("span", class_="num _price_reload") != None:
        price.append(b.find("span", class_="price").find("span", class_="num _price_reload").text)
    else :
        price.append("0")
   


shoppinginfo = []
for i in range(len(box)) :
    shopping = []
    shopping.append(title[i])
    shopping.append(price[i])
    shoppinginfo.append(shopping)

for i in shoppinginfo :
    print(i)

