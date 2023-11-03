import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


'''
------------------------------------------------------------------------------------------------------------------------
                                                **ASSIGNMENTS**
                                                     START
------------------------------------------------------------------------------------------------------------------------
'''
'''-----------------------------
assignment: 1     (1 of 2)
Check that actualList matches
expectedList 
see from loc: 45...
stopped vid @
6:14 / 3:37
Total_time: 9:51
------------------------------'''
'''-----------------------------
assignment: 2     (2 of 2)
Check that 
discount price is < total price
stopped vid @
6:14 / 3:37
Total_time: 9:51
------------------------------'''
'''
------------------------------------------------------------------------------------------------------------------------
                                                **ASSIGNMENTS**
                                                      END  
------------------------------------------------------------------------------------------------------------------------
'''


# global lists...
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []  # populate it dynamically using forloop... see from loc:45...loc:53

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
assert count > 0  # assert checks for un-expected results...like not greater than 0...which means kart_items list would be empty...
# this is why The sleep() function is still needed, to give time to populate list: kart_items

#  XPATH for selecting the buttons
# this concept is called "Chaining of web elements" - when you drill down to reach a target element...
# you're chaining your parent element to the child element...to construct an XPATH dynamically...
# //div[@class='products']/div/div/button
# the kart_items list contains results reflecting this XPATH: //div[@class='products']/div
for kart_item in kart_items:  # now every kart_item reflects  this XPATH:  div/button
    kart_item.find_element(By.XPATH, "div/button").click()  # this will click on all three buttons...
# This is from related code on loc:34:  kart_items = driver.find_elements(By.XPATH, "//div[@class='products']/div")
# XPATH = //div[@class='products']/div/h4   <------this matches 3 elements
    actualList.append(kart_item.find_element(By.XPATH, "h4").text)  # <----here just have to add on h4
time.sleep(3) # just for giving time to populate/append the list...

'''
assignment: 1     (1 of 2)
assert that the expected list matches the actual list...
loc:12-13
'''

assert expectedList == actualList

# img[alt='cart']
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
# <---- line above FAILED previously...NOW IT PASSED...perhaps due to needing more time

# XPATH
# "//button[text()='PROCEED TO CHECKOUT']"
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# common selector for item price...
# this is a <p> tag
# .amount   (class) this won't work because we u=just need three elements per the search above...and returns 6 elements which have the same class
# tr td:nth-child(5) p <---- better to use a CSS_Selector selector...to get to the 5th <td> which serve as columns in a row inside a <table>
# XPATH translation of the above CSS_SELECTOR is: //tr/td[5]/p
# to come up with the selector definition, you must analyze the html at hand...the parent/child html configuration to get to your
# target element
# Sum validation
itemPrices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
itemsSum = 0
for itemPrice in itemPrices:
    itemsSum = itemsSum + int(itemPrice.text)

print(itemsSum)
# class totAmt
# .totAmt
# //span[@class='totAmt']  <-----XPATH version...
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)  # convert str to int...
assert itemsSum == totalAmount  # with assertions, no news is good news!...


# .promoCode
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

# .promoBtn
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()  # if you use CSS_SELECTOR, you must use the . dot with .classname

# time.sleep(5)  # this is normally not used instead use explicit wait or implicit wait...

# create WebDriverWait...
wait = WebDriverWait(driver, 10)  # waiting for 10 seconds...

# waiting for what?  - for this expected condition which is to wait for this element (this CSS_Selector) to load...
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, ".promoInfo")))  # must use . dot when using By.CSS_SELECTOR
# .promoInfo      it will show the text: "Code applied..!" ----waiting for this text to show...
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)  # if you use CLASS_NAME, you don't use the . dot

'''----------------------------------
assignment: 2     (2 of 2)
Check that 
discountAmount price is <totalAmount
<span> tag
Class: .discountAmt
----------------------------------'''
# discountAmount = int(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text) <-----produces error below...
discountAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)  # <-----this works...
assert discountAmount < totalAmount


# PRODUCES ERROR: due to decimal (float) result...expected an integer...
# Traceback (most recent call last):
#  File "C:\Users\Martin\PycharmProjects\pythonTesting\explicitWaitDemo.py", line 141, in <module>
#    discountAmount = int(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
# ValueError: invalid literal for int() with base 10: '349.2'

