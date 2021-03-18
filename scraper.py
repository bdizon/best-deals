# import pyderman as cdi
# path = cdi.install(file_directory='c:\\data\\chromedriver\\', verbose=True, chmod=True, overwrite=False, version=None)
# print('Installed chromedriver to path: %s' % path)
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# creates chromedriver instance pointing to the folder containing the installed chromredriver
# driver = webdriver.Chrome("c:\\users\\bianca dizon\\appdata\\local\\programs\\python\\python38\\python.exe")
# driver = webdriver.Chrome("C:\\Users\\Bianca Dizon\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages\\selenium\\webdriver\\chrome\\webdriver.py")
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# import Selenium2Library
# s = Selenium2Library.Selenium2Library()
# url = s.get_location()
PATH = "C:\Program Files (x86)\chromedriver.exe"
LOC = "877 Tallgrass dr, bartlet, il"
driver = webdriver.Chrome(PATH)
# chrome_options = Options()
# chrome_options.add_experimental_option( "prefs", {'protocol_handler.excluded_schemes.tel': False})
# driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
''' 
FOR GRUBHUB
'''
# open up the website
driver.get("https://www.grubhub.com/")
print(driver.title)
# driver.quit()

# find search box for location and enter user address
addr = driver.find_element_by_name("searchTerm")
addr.clear()
addr.send_keys(LOC)
addr.send_keys(Keys.RETURN)

# wait to update url
time.sleep(2)
# wait = WebDriverWait(driver, 3)
print(driver.current_url)

ITEM = "burger"
# food = driver.find_element_by_name("searchTerm")
# food = driver.find_element_by_id("search-autocomplete-input")
# food = driver.find_element_by_class_name("s-form-control ghs-searchInput input-overflow")
# used xpath since name, id, and class name elements could not be lcoated
food = driver.find_element_by_xpath("/html/body/ghs-site-container/span/span/span[4]/ghs-app-content/div[2]/ghs-main-nav/div[2]/form/div/div[2]/div/input")
food.clear()
food.send_keys(ITEM)
food.send_keys(Keys.RETURN)

# loop through all cards in first page for results that match the name if match cant be found pick first result
# cards = driver.find_elements_by_xpath("/html/body/ghs-site-container/span/span/span[4]/ghs-app-content/div[3]/div/ghs-router-outlet/ghs-search-container/ghs-search/ghs-search/div/div[2]/div/div[2]/div/div/ghs-search-results/div[1]/div/div[4]/div/ghs-impression-tracker/div/div[1]/span/span/div/div/div[2]/div[1]/a/h5")
# i = 0
# for card in cards:
#     print(i)
#     i += 1

print(driver.current_url)
# loop through to get all the results from the first page
# get restaurant name, time, delivery fee, link to webpage to order
# cards = driver.find_elements_by_class_name("u-text-ellipsis")
cards = driver.find_elements_by_class_name("restaurant-name")
resto_name = []
for card in cards:
    print(card.text)
    # remove first card because it contains the location instead of restaurant
    resto_name.append(card.text)
print(resto_name)
