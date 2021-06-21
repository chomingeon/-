from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

search=input('검색어 입력 :')
driver = webdriver.Chrome()

driver.get('https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl')
elem = driver.find_element_by_name('q')
elem.send_keys(search)
elem.send_keys(Keys.RETURN)

directory='./images'
if not os.path.exists(directory):
    os.makedirs(directory)
images =  driver.find_elements_by_css_selector('rg_i Q4LuWd')
count = 1
for i,image in enumerate(images) :
    try :
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_css_selector('.n3VNCb').get_attribute('src')
        urllib.request.urlretrieve(imgUrl, './images/' + search + str(count) + '.jpg')
        count = count + 1
    except:
        break
driver.close()    
