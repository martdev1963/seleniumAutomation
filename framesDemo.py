import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")
# driver below, not working...
# service_obj = Service("C:/Users/Martin/Documents/geckodriver.exe.exe") must reconfigure the other drivers; firefox,edge, etc...

# chrome driver... manually configured way...by providing the path to the downloaded driver...
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/iframe")

# first switch to the iframe...
driver.switch_to.frame("mce_0_ifr") # you can use either ID or name attribute if it's available...
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames...")

# first switch back to parent page...because an iframe is another separate webpage...
driver.switch_to.default_content()  # when driver is initially instantiated, whatever scope its in, it will switch back to that
# normal browser scope...

'''--------------------------------------------------------------------------------------------------------------------
Code below dealing with the unique h3 tag
not running the driver.switch_to.default_content() first, will produce following error:
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: 
{"method":"css selector","selector":"h3"}

Further practice on frames can be had at:
https://rahulshettyacademy.com/AutomationPractice/
<iframe id="courses-iframe" src="https://www.rahulshettyacademy.com/" name="iframe-name" 
style="width: 100%; height: 600px" scrolling="yes" marginwidth="0" marginheight="0" 
vspace="0" hspace="0" frameborder="0">
            </iframe>
--------------------------------------------------------------------------------------------------------------------'''
output = driver.find_element(By.CSS_SELECTOR, "h3").text
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
assert output == "An iFrame containing the TinyMCE WYSIWYG Editor"






