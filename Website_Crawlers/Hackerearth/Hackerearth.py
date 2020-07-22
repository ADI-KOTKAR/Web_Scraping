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

driver.get("https://www.hackerearth.com/challenges/")
#print(driver.title)
data = []

''' Functions '''
def extract():
    try: 
        ul = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.ID,"challenge-container")) 
        ) 
        #print(ul.text)
        lists = ul.find_elements_by_class_name('challenge-list')
        print(lists)
        for li in lists:
            if li.find_elements_by_class_name("challenge-card-modern"):
                cards = li.find_elements_by_class_name("challenge-card-modern")
                for card in cards:
                    print("---------------")
                    title = card.find_element_by_class_name("challenge-list-title")
                    print('Title: ',title.text)
                    data.append([title.text,"", "Hackathon"])
            if li.find_elements_by_class_name("challenge-card"):
                cards = li.find_elements_by_class_name("challenge-card")
                for card in cards:
                    print("---------------")
                    title = card.find_element_by_class_name("challenge-list-title")
                    print('Title: ',title.text)
                    data.append([title.text, "","Hackathon"])

    except: 
        driver.quit()


''' CSV creation '''
extract()
with open('Hackerearth_Dataset.csv','a+', newline='') as fp:
    thewriter = csv.writer(fp)
    thewriter.writerows(data)

time.sleep(10)
driver.quit()
# print(driver.page_source)




