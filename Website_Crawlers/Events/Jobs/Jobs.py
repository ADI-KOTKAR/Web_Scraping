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

driver.get("https://www.timesjobs.com/candidate/job-search.html?from=submit&searchType=Home_Search&luceneResultSize=25&postWeek=60&cboPresFuncArea=35&pDate=Y&sequence=11&startPage=11")
#print(driver.title)
data = []

''' Functions '''
def extract():
    try: 
        ul = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.CLASS_NAME,"new-joblist")) 
        )
        #print(ul.text)
        lists = ul.find_elements_by_class_name('job-bx')
        #print(lists.text)
        for li in lists:
            print("---------------")
            title = li.find_element_by_tag_name("h2")
            print('Title: ',title.text)
            data.append([title.text, ""])
        next_page()
    except: 
        driver.quit()

def next_page():
    try: 
        next_page = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.CLASS_NAME, "nxtC")) 
        ) 
        next_button = next_page.find_element_by_tag_name("a")
        next_button.send_keys(Keys.ENTER)
        extract()
    except: 
        driver.quit() 

''' CSV creation '''
extract()
with open('Jobs.csv','a+', newline='') as fp:
    thewriter = csv.writer(fp)
    thewriter.writerows(data)

time.sleep(10)
driver.quit()
# print(driver.page_source)




