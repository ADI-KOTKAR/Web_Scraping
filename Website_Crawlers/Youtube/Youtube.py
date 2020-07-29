# Import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

import csv

''' Code '''
PATH = 'C:\Program Files (x86)/chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/results?search_query=c#%2C+ruby+on+rails")
#print(driver.title)
data = []
for i in range(0,15):
    driver.execute_script("window.scrollBy(0,10**5)","")
    time.sleep(5)
# page = driver.find_element_by_tag_name("html")
# page.send_keys(Keys.END)

''' Functions '''
def extract():
    try: 
        ul = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]')) 
        ) 
        #print(ul.text)
        lists = ul.find_elements_by_tag_name('h3')
        #print(lists)
        for li in lists:
            print("---------------")
            print('Title: ',li.text)
            data.append([li.text, "other"])
    except: 
        driver.quit()

''' CSV creation '''
extract()
with open('YT_Other.csv','w', newline='', encoding='utf-8') as fp:
    thewriter = csv.writer(fp)
    thewriter.writerows(data)

time.sleep(10)
driver.quit()
# print(driver.page_source)




