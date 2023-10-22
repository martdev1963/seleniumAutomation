from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

# chrome driver... using Selenium Manager which searches and downloads the chromedriver....this is much slower...
service_obj = Service() # create object of Service class...


# chrome driver... manually configured way...by providing the path to the downloaded driver...
service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("martdev1963@gmail.com")

# locator creation as an XPATH...
# //form/div[1]/input

# example below for password field...
# locator creation as an CSSSelector...just get rid slashes...
# form div:nth-child(2) input
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Rocket12!")

# password confirmation input field
# form div:nth-child(3) input  <-----CSSSelector
# //form/div[3]/input  <-------XPATH
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Rocket12!")


# save new password button
# //button[@type='submit']  <------XPATH
# driver.find_element(By.XPATH, "//button[@type='submit']").click()

# use text on button
# //button[text()='Save New Password']
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()














