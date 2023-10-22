from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

# chrome driver... manually configured way...by providing the path to the downloaded driver...
service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")

name = "Martin"
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)  # note using # for CSS_SELECTOR

# alert button
# #alertbtn
driver.find_element(By.ID, "alertbtn").click()  # note not using # for ID...
# alert object doesn't have browser level or browser scope...strictly for alert popup ...it's made with java or javaScript
alert = driver.switch_to.alert  # so you must use driver.switch_to.alert...
alertText = alert.text
print(f" Text from alert popup... {alertText}")
assert name in alertText  # assert is used to see if the test will pass or fail...

# to click on ok button in the alert popup,
alert.accept()  # for clicking the ok button...
# alert.dismiss()  # for clicking on the cancel button in a confirm popup...

