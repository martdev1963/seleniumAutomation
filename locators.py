from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver... using Selenium Manager which searches and downloads the chromedriver....this is much slower...
service_obj = Service() # create object of Service class...


# chrome driver... manually configured way...by providing the path to the downloaded driver...
service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
# driver.get("https://rahulshettyacademy.com")
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Locators supported by selenium:
# ID Xpath CSSSelector Classname, name linkText

# email field input selector:
# body > app-root > form-comp > div > form > div:nth-child(2) > input
# XPAth = /html/body/app-root/form-comp/div/form/div[2]/input


# element: <input class="form-control ng-pristine ng-invalid ng-touched" name="email" required="" type="text">
driver.find_element(By.NAME, "name").send_keys("martdev1963@gmail.com")

# Password field:
# <input class="form-control" id="exampleInputPassword1" placeholder="Password" type="password">
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password123")

# checkbox element:
# <input class="form-check-input" id="exampleCheck1" type="checkbox">
driver.find_element(By.ID, "exampleCheck1").click()

# submit button:
# <input class="btn btn-success" type="submit" value="Submit">
# Syntax for writing Xpath:
# //tagname[@attribute='value'] -----> //input[@type='submit']

# syntax for writing CSSSelector:
# tagname[attribute='value'] -----> input[type='submit']


driver.find_element(By.XPATH, "//input[@type='submit']").click()


# success message upon submitting form:
# <div class="alert alert-success alert-dismissible">
#                     <a aria-label="close" class="close" data-dismiss="alert" href="#">×</a>
#                     <strong>Success!</strong> The Form has been submitted successfully!.
#                   </div>
message = driver.find_element(By.CLASS_NAME, "alert-success").text # grabs text present in the element...
print(message)


# name
# <input class="form-control ng-dirty ng-valid ng-touched" minlength="2" name="name" required="" type="text">

# driver.find_element(By.NAME, "name").send_keys("Martin")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Martin")
assert "Success" in message

# employment status radio buttons:
# <input class="form-check-input" id="inlineRadio1" name="inlineRadioOptions" type="radio" value="option1">

# CSSSelector Syntax:
# input[value='option1']

# XPATH Syntax:
# //input[@value='option1']

# Using an ID do this:  #id
#   #inlineRadio1

# Using a class do this:  .classname
# .alert-success

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()


# if you see a <select> tag then you can use the Select() class...
# Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))

dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)  # selects male option...female is at index 1
# dropdown.select_by_value() <----can assign using the value attribute...




# XPATH Syntax: for identifying multiple elements of the same type attribute for example...
# (//input[@type='text'])[3]

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello again...")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()











