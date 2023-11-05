import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")
# service_obj = Service("C:/Users/Martin/Documents/geckodriver.exe.exe")

# chrome driver... manually configured way...by providing the path to the downloaded driver...
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(9)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

# returns list of windows opened...in the order that they were opened...via indexing as with any list...
windows_opened = driver.window_handles  # this is a property that gets all the window names of all windows that are opened...
driver.switch_to.window(windows_opened[1]) # child tab...
print(f"This is from a (child tab) or new window tab:  {driver.find_element(By.TAG_NAME, 'h3').text}")
driver.close() # close child window or tab...
driver.switch_to.window(windows_opened[0]) # back to parent tab...
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
print(driver.find_element(By.TAG_NAME, "h3").text)
