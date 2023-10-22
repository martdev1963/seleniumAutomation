import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")

# chrome driver... manually configured way...by providing the path to the downloaded driver...
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

# autosuggest dropdown...
# CSSSelector - li[class='ui-menu-item'] a <-------this is a common selector

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

print(f"Number of elements: {len(countries)} elements")
# using for loop to traverse through list of common tag: li[class='ui-menu-item'] a
for country in countries:
    if country.text == "India":
        print(f"Element chosen is: {country.text} ")
        country.click()
        break


# print(driver.find_element(By.ID, "autosuggest").text)  # this will print nothing because text being grabbed is not static
# print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))  # this method works on dynamic text...
# uses the js DOM value property...
# QA interview question: when updating value dynamically through the script, how do you extract the text?
# use the get_attribute() function

# assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "iuweiruyIndia" #  <------ this will fail

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"  # <------ this will pass



