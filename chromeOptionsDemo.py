import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# chrome driver... manually configured way...by providing the path to the downloaded driver...
service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")

# create object of type ChromeOptions...denoting how the browser should behave when invoked...
# in this case, it will only run in the back-end without being invoked due to headless flag... loc:13
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(service=service_obj, options=chrome_options)

#  "C:/Users/Martin/Documents/chromedriver.exe"
# code below doesn't work...
# driver = webdriver.Chrome(executable_path="C:/Users/Martin/Documents/chromedriver.exe", options=chrome_options)
# causes this error: TypeError: __init__() got an unexpected keyword argument 'executable_path'
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)  # shows <title> tag text...









