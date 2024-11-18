# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from selenium.webdriver.chrome.service import Service
pchomeResult=[]
skey=input("PChome搜尋的商品 :")
n=eval(input("取回數量 :"))
#以下三行關閉 Chrome的"自動軟體測試"提醒
options = Options()
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])

driver=webdriver.Chrome(options)

#driver.get("https://24h.pchome.com.tw/search/?q="+skey)
driver.get("https://24h.pchome.com.tw/")
driver.find_element(By.CLASS_NAME,"c-search__input").send_keys(skey)
driver.find_element(By.CLASS_NAME,"btn--sm").click()

locate=(By.CLASS_NAME,"c-boxGrid")

WebDriverWait(driver,20,1).until(EC.presence_of_element_located(locate))

#print(driver.page_source)

result=driver.page_source
soup=BeautifulSoup(result,"html.parser")

descps=soup.select("div.c-prodInfoV2__title")
prices=soup.select("div.c-prodInfoV2__priceValue.c-prodInfoV2__priceValue--m")


#print(prices)

for i in range(min(n, len(descps))):
    product_name = descps[i].get_text().strip() #if descps else 'No product name found'
    product_price = prices[i].get_text().strip() #if prices else 'No price found'
    print("第  {:d} 項".format(i+1))
    print(f" {product_name}, \n Price: {product_price}")
    print()
        

# Close the driver
driver.quit()