import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")

# chrome driver... manually configured way...by providing the path to the downloaded driver...
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "(//input[@type='checkbox'])") # returns a list of said element...
print(f"There are  {len(checkboxes)} returned... ")

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        print(f"option returned is: {checkbox.get_attribute('value')}")
        checkbox.click()
        assert checkbox.is_selected()  # boolean function...
        break

radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")  # returns a list of said element...
# radioButtons[2].click()

print(f"There are {len(radioButtons)} radio buttons returned... ")

for radioButton in radioButtons:
    if radioButton.get_attribute("value") == "radio3":
        print(f"radioBut returned is: {radioButton.get_attribute('value')}")
        radioButton.click()
        assert radioButton.is_selected()  # if not selected, assertion will fail...
        break


# create XPATH for radio button (trying to get radio2)
# (//input[@type='radio'])[2]  # selects radio button 3... indexes 0, 1, 2
# using the class attribute:
# .radioButton:nth-child(2)  # selects radio button 2...


# create XPATH locator:
# if id, value, or name attributes weren't available then do this:
# (//input[@type='checkbox'])[2] # selects option 2 checkbox...
# (//input[@type='checkbox'])  # this returns 3 checkboxes...

# is displayed...
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()  # clicks on hide button thus hiding the field
assert not driver.find_element(By.ID, "displayed-text").is_displayed()  # using negation...

'''
NEXT LECTURE: Handling Java / JavaScript Alert popups using Selenium...
9:00 min
lecture number: lectures/13248307
'''


