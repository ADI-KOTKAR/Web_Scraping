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

driver.get("http://free.aicte-india.org/")
#print(driver.title)
data = []

''' Functions '''
def extract():
    try: 
        ul = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.CLASS_NAME,"course-area")) 
        )
        #print(ul.text)
        lists = ul.find_elements_by_class_name('col-md-4')
        #print(lists.text)
        for li in lists:
            print("---------------")
            title = li.find_element_by_tag_name("h4")
            print('Title: ',title.text)
            data.append([title.text, ""])
    except: 
        driver.quit()


''' CSV creation '''
extract()
with open('AICTE_Dataset.csv','a+', newline='') as fp:
    thewriter = csv.writer(fp)
    thewriter.writerows(data)

time.sleep(10)
driver.quit()
# print(driver.page_source)




