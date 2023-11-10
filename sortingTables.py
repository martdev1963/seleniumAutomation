import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# chrome driver... manually configured way...by providing the path to the downloaded driver...
service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# empty list
browserSortedVeggies = []


# click on column header
# XPATH syntax for grabbing text from html tag...
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()  # by clicking on header text, this sorts the list...
# create a list...
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

# the list that got sorted by the browser functionality when header text got clicked above...
# slice() also works like copy() but copy() is faster than slice() and newer...
# originalBrowserSortedList = browserSortedVeggies.slice()
originalBrowserSortedList = browserSortedVeggies.copy()  # assign original list sorted by browser to originalBrowserSortedList list...
# purpose of this is to be able to truly make a comparison between the browser sort functionality and selenium sort() result...
# thus effectively testing/checking that the browser sorting function worked properly...thus passing this "testcase"

# sort this browserSortedVeggies list  (alphabetical order)
browserSortedVeggies.sort()

# now compare original browser sorted list to selenium sorted list...
assert browserSortedVeggies == originalBrowserSortedList
