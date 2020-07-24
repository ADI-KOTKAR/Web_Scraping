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

driver.get("https://dare2compete.com/e/competitions/all")
driver.maximize_window()

# for i in range(0,700):
#     driver.execute_script("window.scrollBy(0,10**5)","")
#     time.sleep(5)

#print(driver.title)
data = []

''' Functions '''
def extract():
    try: 
        ul = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/app-explore/section/div/div[2]/div[3]/app-opportunity-listbox/div")) 
        )
        #print(ul.text)
        #time.sleep(200)
        lists = ul.find_elements_by_class_name('title')
        #print(lists.text)
        for li in lists:
            print("---------------")
            # h = li.find_element_by_tag_name("h2")
            title = li.find_element_by_tag_name("h2")
            print('Title: ',title.text)
            data.append([title.text, "Competitions"])
    except: 
        driver.quit()


''' CSV creation '''
time.sleep(720)
extract()
def CSV(data):
    with open('Competitions.csv','a+', newline='',encoding="utf-8") as fp:
        thewriter = csv.writer(fp)
        thewriter.writerows(data)
CSV(data)


driver.quit()
# print(driver.page_source)




