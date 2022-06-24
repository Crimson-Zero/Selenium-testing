from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "path"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a")
#article_count.click()

all_portals = driver.find_element_by_link_text("Content portals")
all_portals.click()

#type in search bar

search = driver.find_element_by_name("search")
search.send_keys("Python")

#send uncommon keys example enter shift etc

search.send_keys(Keys.ENTER)
