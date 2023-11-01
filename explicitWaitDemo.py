import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")

# chrome driver... manually configured way...by providing the path to the downloaded driver...
driver = webdriver.Chrome(service=service_obj)

# implicit Wait is a global timeout...
driver.implicitly_wait(5)  # 5 sec is the max timeout here...but if pertinent code runs before 5 secs, it will go with that...
# it differs from sleep() function because sleep() function will wait for specified time...

# lecture in section 12: What are waits?
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")  # typing ber yield's 3 items
time.sleep(2)  # to give server time to load items... The sleep() function is still needed to give time to populate list: kart_items

# USING XPATH Selector...
# //div[@class='products']/div  this is the parent selector: <div class="products"></div>
# which currently contains 3 items...based on whats typed above (ber...)
# return a list of child items:
kart_items = driver.find_elements(By.XPATH, "//div[@class='products']/div")  # using plural version...returns list of products...the 3 from the search: ber
count = len(kart_items)  # should be > 0 else there is a bug in the functionality...
# print(len(kart_items))
assert count > 0 # assert checks for un-expected results...like not greater than 0...which means kart_items list would be empty...
# this is why The sleep() function is still needed, to give time to populate list: kart_items

#  XPATH for selecting the buttons
# this concept is called "Chaining of web elements" - when you drill down to reach a target element...
# you're chaining your parent element to the child element...to construct an XPATH dynamically...
# //div[@class='products']/div/div/button
# the kart_items list contains results reflecting this XPATH: //div[@class='products']/div
for kart_item in kart_items:  # now every kart_item reflects  this XPATH:  div/button
    kart_item.find_element(By.XPATH, "div/button").click()  # this will click on all three buttons...

# img[alt='cart']
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
# <---- line above FAILED previously...NOW IT PASSED...perhaps due to needing more time

# XPATH
# "//button[text()='PROCEED TO CHECKOUT']"
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# .promoCode
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

# .promoBtn
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()  # if you use CSS_SELECTOR, you must use the . dot with .classname

# time.sleep(5)  # this is normally not used instead use explicit wait or implicit wait...

# create WebDriverWait...
wait = WebDriverWait(driver, 10)  # waiting for 10 seconds...

# waiting for what?  - for this expected condition which is to wait for this element (this CSS_Selector) to load...
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, ".promoInfo")))  # must use . dot when using By.CSS_SELECTOR
# .promoInfo
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)  # if you use CLASS_NAME, you don't use the . dot
