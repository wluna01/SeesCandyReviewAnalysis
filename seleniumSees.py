import os
import sys
import time 
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

#open chrome browser automation
browser = webdriver.Chrome('/Users/Will/Desktop/chromedriver',options=options)
browser.get('https://www.sees.com/chocolate/nuts-and-chews/assortment/200392.html?cgid=assortments')
browser.implicitly_wait(100)
time.sleep(1)

#click load button, wait one second for page to load, repeat
counter = 0
while (counter < 290): #
	time.sleep(1)
	browser.implicitly_wait(100)
	elem = browser.find_element_by_link_text('LOAD MORE')
	elem.click()
	counter+=1

tutorial_soup = BeautifulSoup(browser.page_source, 'html.parser')

#save the webpage as a html file
with open("nuts_chews_reviews.html", "w") as f:
	f.write(browser.page_source)
