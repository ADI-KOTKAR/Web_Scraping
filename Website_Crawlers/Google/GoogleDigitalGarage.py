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

driver.get("https://learndigital.withgoogle.com/digitalgarage/courses")
#print(driver.title)
data = []

''' filters '''
# 0 - Data and Tech, 1 - Digital Marketing, 2 - Career Development
filters = driver.find_elements_by_tag_name("md-checkbox")
filters[0].send_keys(Keys.ENTER)

''' Functions '''
def extract():
    try: 
        ul = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.CLASS_NAME,"course-list__cards")) 
        ) 
        #print(ul.text)
        lists = ul.find_elements_by_class_name('course-list__cards__card')
        #print(lists.text)
        for li in lists:
            print("---------------")
            title = li.find_element_by_class_name("course-card__title")
            print('Title: ',title.text)
            data.append([title.text, "Data and Tech"])
    except: 
        driver.quit()


''' CSV creation '''
extract()
with open('GoogleDigitalGarage.csv','a+', newline='') as fp:
    thewriter = csv.writer(fp)
    thewriter.writerows(data)

time.sleep(10)
driver.quit()
# print(driver.page_source)




