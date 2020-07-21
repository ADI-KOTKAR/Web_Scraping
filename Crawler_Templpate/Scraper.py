# Import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# Code
PATH = 'C:\Program Files (x86)/chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://online-learning.harvard.edu/")
#print(driver.title)

search = driver.find_element_by_id("edit-keywords")
search.send_keys("css")
search.send_keys(Keys.RETURN)

try: 
    ul = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.CLASS_NAME, "course-grid")) 
    ) 
    li = ul.find_elements_by_class_name("views-row")
    print(li.text)
    div1 = li.find_elements_by_class_name("entity")
    print(div1.text)
    
except: 
    driver.quit() 




# print(driver.page_source)

time.sleep(10)
driver.quit()


