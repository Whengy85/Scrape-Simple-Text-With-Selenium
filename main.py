from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("start-maximized")
options.add_argument() # Left Off Here
driver = webdriver.Chrome()

print("Hello")