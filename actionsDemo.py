import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")

# chrome driver... manually configured way...by providing the path to the downloaded driver...
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
# action.click_and_hold()
# action.double_click(driver.find_element(By.CSS_SELECTOR))  # note the syntax for usage...(works on checkboxes??)
# action.context_click()  # this stands for right-click...
# action.drag_and_drop()

# id
# mousehover
#  it will just move to that particular element...it won't perform any click or other operation...
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()  # must also use perform() at end for all actions...
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
