from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "/7th/chromedriver"
driver = webdriver.Chrome(path)

try :
    driver.get("https://www.coupang.com/")
    time.sleep(1)

    searchIndex = "청바지"
    element = driver.find_element_by_class_name("coupang-search")
    element.send_keys(searchIndex)
    driver.find_element_by_class_name("search").click()

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    pages = int(bs.find("a", class_ = "btn-last disabled").text)
    print(pages)
    
    title = []


    for i in range(2) : 
        time.sleep(1)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find("div", class_ = "search-content search-content-with-feedback").find_all("dl", class_ = "search-product-wrap")

        title.append("page" + str(i + 1))
        for c in conts :
            title.append(c.find("div", class_ = "descriptions-inner").find("div", class_ = "name").text)
        
        driver.find_element_by_xpath('//*[@id="searchOptionForm"]/div[2]/div[2]/div[4]/a[2]').click()

finally :
    for t in title :
        if t.find("page") != -1 :
            print()
            print(t)
        else :
            print(t)


    driver.quit()
