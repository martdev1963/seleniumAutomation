import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait  # for explicit waits...

# object of type ChromeOptions()...
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")

# Service object
service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")
# driver below, not working...
# service_obj = Service("C:/Users/Martin/Documents/geckodriver.exe.exe") must reconfigure the other drivers; firefox,edge, etc...

# chrome driver object... manually configured way...by providing the path to the downloaded driver...
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(4)  # setting global timeout using implicit wait...


driver.get("https://rahulshettyacademy.com/angularpractice/")

# regular expression syntax:
# //a[contains(@href, 'shop')]  # passing attribute and only a partial value...
# CSS SELECTOR: a[href*='shop']
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

# using chaining of parent/child elements here...
# XPATH
# //div[@class='card h-100']
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    # //div[@class='card h-100']/div/h4/a
    product_name = product.find_element(By.XPATH, "div/h4/a").text  # This "/div/h4/a" results in error: remove extra /
    if product_name == "Blackberry":
        # //div[@class='card h-100']/div/button
        product.find_element(By.XPATH, "div/button").click()  # This "/div/button" results in error: remove extra /

# a[class*='btn-primary']
# driver object traverses the whole page to find element...
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

# //button[@class='btn btn-success']
# Alternative to using SelectorsHub: use the console of DevTools... $x()  the x is for XPATH:
# $x("//button[@class='btn btn-success']")
# for CSS validation, no need to write x just $() is enough:
# $("button[@class='btn btn-success']")
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")

# explicit wait object...
wait = WebDriverWait(driver, 10)  # wait 10 seconds to give time to load auto suggestions...
# note here you just pass the locator: By.LINK_TEXT no need to driver.find_element...presence_of doesn't take web elements...
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

# XPATH for checkbox...
# //div[@class='checkbox checkbox-primary']
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

# CSS SELECTOR for purchase button:
# you don't always have to use the tab name, you can just do this: [type='submit'] if there's only one of these
# if there are mor, then you have to use the tag name like the example below:
#  input[type='submit']  <----- this will make it unique
# //input[@class='btn btn-success btn-lg']

driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
# <div class="alert alert-success alert-dismissible">
#           <a aria-label="close" class="close" data-dismiss="alert" href="#">×</a>
#           <strong>Success!</strong> Thank you! Your order will be delivered in next few weeks :-).
#         </div>

# CSS SELECTOR
# div[@class='alert alert-success alert-dismissible']
success_text = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in success_text

driver.close()











