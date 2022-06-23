from selenium import webdriver

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/dp/B01NBKTPTS")

scrap_price = driver.find_element_by_id("corePrice_feature_div")

price = scrap_price.text
