from selenium import webdriver

chrome_driver_path = "path"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")
search_bar = driver.find_element_by_name("q") #name in the html element

print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element_by_class_name("python-logo")

print(logo.size)

css_selector = driver.find_element_by_css_selector(".documentation-widget a")
print(css_selector.text)

x_path = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a') #for those not having unique attributes
print(x_path.text)
driver.close()
