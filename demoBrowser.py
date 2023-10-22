from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.edge.service import Service

'''
Current Lecture on this laptop:
https://courses.rahulshettyacademy.com/courses/17128/lectures/13247878
Basic webdriver methods part 2: refresh,frwd, minimizeWindow...
'''


# chrome driver... using Selenium Manager which searches and downloads the chromedriver....this is much slower...
service_obj = Service()  # the Service class starts and stops the chrome driver service...
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://rahulshettyacademy.com")


# firefox driver
# driver = webdriver.Firefox(service=service_obj)
# driver.get("https://rahulshettyacademy.com")


# edge driver
# driver = webdriver.Edge(service=service_obj)
# driver.get("https://rahulshettyacademy.com")


# chrome driver... manually configured way...
# service_obj = Service("C:\Users\Martin\Documents\chromedriver.exe")  # <----wrong slashes...
service_obj = Service("C:/Users/Martin/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Firefox
# service_obj = Service("C:/Users/Martin/Documents/geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)

# Microsoft Edge
# service_obj = Service("C:/Users/Martin/Documents/msedgedriver.exe")
# driver = webdriver.Chrome(service=service_obj)






driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()












