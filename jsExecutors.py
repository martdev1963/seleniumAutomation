import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# object of type ChromeOptions()...
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")
# driver below, not working...
# service_obj = Service("C:/Users/Martin/Documents/geckodriver.exe.exe") must reconfigure the other drivers; firefox,edge, etc...

# chrome driver... manually configured way...by providing the path to the downloaded driver...
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(2)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# JavaScript code to inject...
# there are many function options to choose from...once you type window. you will see them listed...

# window.scrollTo(0,600)
# window.scrollBy(0.Document.body.scrollHeight)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")  # selenium function for injecting JavaScript...
driver.get_screenshot_as_file("screenshotOfBottom.png")  # just name the file first (in quotes) for the screenshot...
#  in the folder level, you will then see a screenshot captcher, after it scrolls. (due to running the previous scrollBy() code)

