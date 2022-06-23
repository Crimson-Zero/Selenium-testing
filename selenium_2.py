from selenium import webdriver

chrome_driver_path = "C:/Development/chromedriver.exe"

time_array = []
event_array=[]

output_dict = {}
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")

get_time = driver.find_element_by_css_selector(".event-widget ul")
other=get_time.text

get_array = other.split('\n')
print(get_array)

for i in range(len(get_array)):
    if (i%2==0):
        time_array.append(get_array[i])
    else:
        event_array.append(get_array[i])
        

print(time_array)
print(event_array)

for j in range(len(time_array)):
    another_dict = {
        j:
            {
                "time":time_array[j],
                "name":event_array[j]
            }
            
            }
    output_dict.update(another_dict)

print(output_dict)
