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

driver.get("https://www.eduonix.com/courses/Mobile-Development")
#print(driver.title)
data = []

''' Functions '''
def extract():
    try: 
        ul = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.CLASS_NAME, "catLogthumb")) 
        ) 
        #print(ul.text)
        lists = ul.find_elements_by_class_name('divThumbHeadSecondary')
        #print(lists.text)
        for li in lists:
            print("---------------")
            #title = li.find_element_by_tag_name("h3")
            #field = li.find_element_by_class_name("field-name-subject-area")
            #print('Field: ',field.text)
            print('Title: ',li.text)
            #data.append([title.text, field.text])
        #next_page()
    except: 
        driver.quit()

def next_page():
    try: 
        next_page = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.CLASS_NAME, "pagination")) 
        ) 
        next_button = next_page.find_element_by_link_text("Next")
        next_button.send_keys(Keys.ENTER)
        #extract()
    except: 
        driver.quit() 


''' CSV creation '''
#extract()
next_page()
# with open('Udemy_Dataset.csv','w', newline='') as fp:
#     thewriter = csv.writer(fp)
#     thewriter.writerows(data)

time.sleep(10)
driver.quit()
# print(driver.page_source)




