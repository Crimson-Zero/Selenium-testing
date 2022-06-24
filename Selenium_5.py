from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "path"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")


fname = driver.find_element_by_name("fName")
fname.send_keys("testing")

lname = driver.find_element_by_name("lName")
lname.send_keys("second test")

email = driver.find_element_by_name("email")
email.send_keys("xyz@hotmail.com")


button = driver.find_element_by_tag_name("button")
button.send_keys(Keys.ENTER)
