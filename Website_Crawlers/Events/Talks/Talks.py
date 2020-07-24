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

driver.get("https://dare2compete.com/editors-pick")
#print(driver.title)
data = []
count=1
''' Functions '''
def extract():
    try: 
        ul = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.CLASS_NAME, "my_sect")) 
        ) 
        #print(ul.text)
        lists = ul.find_elements_by_class_name('cptn')
        #print(lists.text)
        for li in lists:
            try:
                print("---------------")
                title = li.find_element_by_tag_name("h2")
                print('Title: ',title.text)
                data.append([title.text, "Talks"])
                print("data")
            except:
                continue
        print("done")
        CSV(data)
        data.clear()
        time.sleep(10)
        next_page()
    except: 
        driver.quit()

def next_page():
    global count
    if count < 18:
        try:
            count += 1
            page = driver.find_element_by_class_name("pagination")
            next_button = page.find_element_by_link_text(str(count))
            driver.execute_script("arguments[0].click();", next_button)
            #extract()
            time.sleep(10)
            extract()
        except: 
            driver.quit()
    return      
        



''' CSV creation '''
#extract()
def CSV(data):
    with open('Talks.csv','a+', newline='',encoding="utf-8") as fp:
        thewriter = csv.writer(fp)
        thewriter.writerows(data)
time.sleep(10)
extract()
driver.quit()
# print(driver.page_source)




