import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
driver.implicitly_wait(4)


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
        product.find_element(By.XPATH, "div/button").click() # This "/div/button" results in error: remove extra /
    if product_name == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()


# a[class*='btn-primary']
# driver object traverses the whole page to find element...
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()






